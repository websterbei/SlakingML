/*
* @Author: Webster Bei Yijie, Joey Junyu Liang
* @Date: 5/8/2020, 3:02:14 PM
* @Email: yijie.bei@duke.edu, junyu.liang@duke.edu
*/


var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

module.exports = router;
