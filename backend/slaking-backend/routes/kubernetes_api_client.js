/*
* @Author: Webster Bei Yijie, Joey Junyu Liang
* @Date: 5/8/2020, 3:02:22 PM
* @Email: yijie.bei@duke.edu, junyu.liang@duke.edu
*/


const k8s = require('@kubernetes/client-node');
const fs = require('fs');

const kc = new k8s.KubeConfig();
kc.loadFromFile('./routes/kubernetes_config.yml');
const CoreV1Api = kc.makeApiClient(k8s.CoreV1Api);
const BatchV1Api = kc.makeApiClient(k8s.BatchV1Api);
const ExtensionsV1beta1Api = kc.makeApiClient(k8s.ExtensionsV1beta1Api);

module.exports = {
    CoreV1Api,
    BatchV1Api,
    ExtensionsV1beta1Api
};