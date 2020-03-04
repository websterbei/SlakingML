var express = require('express');
var router = express.Router();
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
        res.send({jobs: dbres});
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
      dbres.job_id = jobId;
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
  db = req.app.locals.dbClient.db("jobs");

  var jobObject = {
    data_config: dataConfig,
    model_config: modelConfig,
    model_name: modelName,
    author_name: authorName
  };

  db.collection("jobs").insertOne(jobObject, function(err, dbres) {
    if (err) {
      res.status(500);
      res.send({status: "Failed to submit job"});
    } else {
      trainingJobIdString = dbres.insertedId.toString();
      trainingJobDeploymentYamlString = yamlTemplates.getTrainingDeploymentYaml(trainingJobIdString);
      const trainingJobDeploymentYaml = k8s.loadYaml(trainingJobDeploymentYamlString);
      k8sApi.BatchV1Api.createNamespacedJob('default', trainingJobDeploymentYaml).then((response) => {
        res.send({job_id: trainingJobIdString, training_job_status: "deployed"});
      },
      (err) => {
        console.log(err);
        res.send({status: "Failed to start training"});
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
      res.send({status: "Failed to remove job"});
    } else {
      res.send({status: "successful"});
    }
  });
});

module.exports = router;
