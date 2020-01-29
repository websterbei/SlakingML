var express = require('express');
var router = express.Router();
var ObjectID = require('mongodb').ObjectID;
var cors = require('cors');

/* GET jobs listing. */
router.get('/', function(req, res, next) {
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
router.get('/:jobId', function(req, res, next) {
  jobId = req.params.jobId;
  db = req.app.locals.dbClient.db("jobs");
  db.collection("jobs").findOne({"_id": ObjectID(jobId)}, function(err, dbres) {
    if (err) {
      res.status(500);
      res.send("Failed to retrieve the list of jobs!");
    } else {
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

  console.log(jobObject);

  db.collection("jobs").insertOne(jobObject, function(err, dbres) {
    if (err) {
      res.status(500);
      res.send("Failed to submit the job!")
    } else {
      res.send({job_id: dbres.insertedId.toString()});
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
      res.send("Failed to retrieve the list of jobs!");
    } else {
      res.send({status: "successful"});
    }
  });
});

module.exports = router;
