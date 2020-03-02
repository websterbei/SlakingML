var express = require('express');
var router = express.Router();
var ObjectID = require('mongodb').ObjectID;
var cors = require('cors');

const yamlTemplates = require('./yaml_templates')
const k8s = require('@kubernetes/client-node');
const k8sApi = require('./kubernetes_api_client');


/* GET method to list all deployments */
router.get('/', cors(), function(req, res, next) {
    k8sApi.CoreV1Api.listNamespacedService("default").then((response) => {
        model_deployment_entries = response.response.body.items.filter((item) => {
            return item.metadata.name.startsWith("model-deployment") ? true : false;
        });
        deployed_model_endpoints = model_deployment_entries.map((item) => {
            try {
                return {
                    job_id: item.metadata.name.substring('model-deployment-'.length),
                    endpoint: item.status.loadBalancer.ingress[0].ip + '/predict'
                };
            } catch(error) {
                return {
                    job_id: item.metadata.name.substring('model-deployment-'.length),
                    endpoint: "Pending"
                };
            }
        });
        res.send(deployed_model_endpoints);
    },
    (err) => {
        console.log(err);
        res.status(500);
        res.send("Failed to look up for deployments!");
    });
});

/* PUT method to create a deployment from a job id */
router.put('/:jobId', cors(), function(req, res, next) {
    jobId = req.params.jobId;
    db = req.app.locals.dbClient.db("jobs");
    db.collection("jobs").findOne({"_id": ObjectID(jobId)}, function(err, dbres) {
        if (err) {
          res.status(404);
          res.send("The given job id does not exist in database!");
        } else {
            modelDeploymentYamlString = yamlTemplates.getModelDeploymentYaml(jobId);
            const modelDeploymentYaml = k8s.loadYaml(modelDeploymentYamlString);
            k8sApi.ExtensionsV1beta1Api.createNamespacedDeployment('default', modelDeploymentYaml).then((response) => {
                deploymentExposureYamlString = yamlTemplates.getModelDeploymentServiceYaml(jobId);
                const deploymentExposureYaml = k8s.loadYaml(deploymentExposureYamlString);
                k8sApi.CoreV1Api.createNamespacedService("default", deploymentExposureYaml).then((response) => {
                    res.send({job_id: jobId, deployment_status: "deployed"});
                },
                (err) => {
                    console.log(err);
                    res.status(500);
                    res.send("Failed to expose deployed service!")
                });
            },
            (err) => {
              console.log(err);
              res.status(500);
              res.send("Failed to create deployment!");
            });
        }
      });
});

module.exports = router;