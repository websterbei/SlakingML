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
        modelDeploymentEntries = response.response.body.items.filter((item) => {
            return item.metadata.name.startsWith("model-deployment") ? true : false;
        });
        deployedModelEndpoints = modelDeploymentEntries.map((item) => {
            try {
                return {
                    model_name: item.metadata.annotations.modelName,
                    job_id: item.metadata.name.substring('model-deployment-'.length),
                    endpoint: item.status.loadBalancer.ingress[0].ip + ':5000/predict'
                };
            } catch(error) {
                return {
                    model_name: item.metadata.annotations.modelName,
                    job_id: item.metadata.name.substring('model-deployment-'.length),
                    endpoint: "Pending"
                };
            }
        });
        res.send(deployedModelEndpoints);
    },
    (err) => {
        console.log(err);
        res.status(500);
        res.send({status: "Failed to lookup deployments"});
    });
});

/* PUT method to create a deployment from a job id */
router.put('/:jobId', cors(), function(req, res, next) {
    jobId = req.params.jobId;
    db = req.app.locals.dbClient.db("jobs");
    db.collection("jobs").findOne({"_id": ObjectID(jobId)}, function(err, dbres) {
        if (err) {
          res.status(500);
          res.send({status: "Failed to lookup for the given job!"});
        } else if (dbres == null) {
          res.status(404);
          res.send({status: "Job does not exist in the database!"});
        } else {
            modelDeploymentYamlString = yamlTemplates.getModelDeploymentYaml(jobId, dbres.model_name);
            const modelDeploymentYaml = k8s.loadYaml(modelDeploymentYamlString);
            k8sApi.ExtensionsV1beta1Api.createNamespacedDeployment('default', modelDeploymentYaml).then((response) => {
                deploymentExposureYamlString = yamlTemplates.getModelDeploymentServiceYaml(jobId, dbres.model_name);
                const deploymentExposureYaml = k8s.loadYaml(deploymentExposureYamlString);
                k8sApi.CoreV1Api.createNamespacedService("default", deploymentExposureYaml).then((response) => {
                    res.send({status: "successful"});
                },
                (err) => {
                    console.log(err);
                    res.status(500);
                    res.send({status: "Failed to create service"});
                });
            },
            (err) => {
              console.log(err);
              res.status(500);
              res.send({status: "Failed to create deployment"});
            });
        }
      });
});


/* DELETE method to remove a deployment */
router.delete('/:jobId', cors(), function(req, res, next) {
    jobId = req.params.jobId;
    deploymentName = `model-deployment-${jobId}`;
    k8sApi.CoreV1Api.deleteNamespacedService(deploymentName, 'default').then((response) => {
        k8sApi.ExtensionsV1beta1Api.deleteNamespacedDeployment(deploymentName, 'default', undefined, undefined, undefined, undefined, 'Background').then((response) => {
            res.send({status: "successful"});
        },
        (error) => {
            res.status(500);
            console.log(error);
            res.send({status: `Failed to remove deployment ${deploymentName}`}); 
        });
    },
    (err) => {
        res.status(500);
        res.send({status: `Failed to remove service ${deploymentName}`});
    });
});

module.exports = router;