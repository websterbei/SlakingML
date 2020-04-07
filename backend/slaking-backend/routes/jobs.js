var express = require('express');
var router = express.Router();
var async = require('async');
var ObjectID = require('mongodb').ObjectID;
var cors = require('cors');

const yamlTemplates = require('./yaml_templates')
const k8s = require('@kubernetes/client-node');
const k8sApi = require('./kubernetes_api_client');

/* GET jobs listing. */
router.get('/', cors(), function(req, res, next) {
  db = req.app.locals.dbClient.db("jobs");
  if(req.query.details!="true") {
    db.collection("jobs").distinct("_id", {}, function(err, dbres) {
      if (err) {
        res.status(500);
        res.send("Failed to retrieve the list of jobs!");
      } else {
        res.send({jobs: dbres});
      }
    });
  } else {
    db.collection("jobs").find({}).toArray(function(err, dbres) {
      if (err) {
        res.status(500);
        res.send("Failed to retrieve the list of jobs!");
      } else {
        jobDetails = [];
        for(var job of dbres) {
          jobDetails.push({
            job_id: job._id,
            data_config: job.data_config,
            model_config: job.model_config,
            model_name: job.model_name,
            author_name: job.author_name,
            status: job.status 
          });
        }
        res.send({jobs: jobDetails});
      }
    });
  };
});


/* GET details about a specific job */
router.get('/:jobId', cors(), function(req, res, next) {
  jobId = req.params.jobId;
  db = req.app.locals.dbClient.db("jobs");
  db.collection("jobs").findOne({"_id": ObjectID(jobId)}, function(err, dbres) {
    if (err) {
      res.status(500);
      res.send({status: "Failed to retrieve job list"});
    } else {
      if(dbres) {
        dbres.job_id = jobId;
      }
      res.send(dbres);
    }
  });
});

/* POST submit a new job */
router.post('/', cors(), function(req, res, next) {
  dataConfig = req.body.data_config;
  modelConfig = req.body.model_config;
  modelName = req.body.model_name;
  authorName = req.body.author_name;
  trainingConfig = JSON.parse(req.body.training_config || "{}");
  db = req.app.locals.dbClient.db("jobs");

  var jobObject = {
    data_config: dataConfig,
    model_config: modelConfig,
    training_config: trainingConfig,
    model_name: modelName,
    author_name: authorName
  };

  db.collection("jobs").insertOne(jobObject, function(err, dbres) {
    if (err) {
      res.status(500);
      res.send({status: "Failed to submit job"});
    } else {
      trainingJobIdString = dbres.insertedId.toString();
      if(trainingConfig.num_trainer > 1) {
        trainingJobDeploymentYamlString = yamlTemplates.getDistributedTrainingDeploymentYaml(trainingJobIdString, modelName, trainingConfig.num_trainer);
      } else {
        trainingJobDeploymentYamlString = yamlTemplates.getTrainingDeploymentYaml(trainingJobIdString, modelName);
      }
      trainingJobDeploymentYaml = k8s.loadYaml(trainingJobDeploymentYamlString);
      k8sApi.BatchV1Api.createNamespacedJob('default', trainingJobDeploymentYaml).then((response) => {
        res.send({job_id: trainingJobIdString, training_job_status: "deployed"});
      },
      (err) => {
        console.log(err);
        // TODO: remove already launched jobs
        res.status(500);
        res.send({status: "Failed to launch training job"});
      });
    }
  });
});


/* DELETE remove a job */
router.delete('/:jobId', cors(), function(req, res, next) {
  jobId = req.params.jobId;
  db = req.app.locals.dbClient.db("jobs");
  db.collection("jobs").deleteOne({"_id": ObjectID(jobId)}, function(err, dbres) {
    if (err) {
      res.status(500);
      res.send({status: "Failed to remove job from database"});
    } else {
      trainingJobName = `model-training-${jobId}`;
      k8sApi.BatchV1Api.deleteNamespacedJob(trainingJobName, 'default', undefined, undefined, undefined, undefined, 'Background').then((response) => {
        res.send({status: "successful"});
      },
      (err) => {
        res.status(500);
        res.send({status: "Failed to remove job from kubernetes"});
      });
    }
  });
});

module.exports = router;
