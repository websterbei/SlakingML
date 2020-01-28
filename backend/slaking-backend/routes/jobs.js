var express = require('express');
var router = express.Router();

/* GET jobs listing. */
router.get('/', function(req, res, next) {
  res.json({jobs: ["1", "2", "3", "4"]});
});

router.get('/:jobId', function(req, res, next) {
  jobId = req.params.jobId;
  res.json({job_id: jobId, job_name: "myjob", job_status: "running", model_location: "here", data_location: "there", training_result_location: "no result yet"});
});

module.exports = router;
