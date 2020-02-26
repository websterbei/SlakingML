var express = require('express');
var router = express.Router();
var cors = require('cors');
const k8sApi = require('./kubernetes_api_client');

/* Testing kubernetes api */
router.get('/allpods', cors(), function(req, res, next) {
    k8sApi.listNamespacedPod('default').then((data) => {
      res.send(data.body);
    });
  });

  module.exports = router;