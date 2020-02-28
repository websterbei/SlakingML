const k8s = require('@kubernetes/client-node');
const fs = require('fs');

const kc = new k8s.KubeConfig();
kc.loadFromFile('./routes/kubernetes_config.yml');
const CoreV1Api = kc.makeApiClient(k8s.CoreV1Api);
const BatchV1Api = kc.makeApiClient(k8s.BatchV1Api);

module.exports = {
    CoreV1Api,
    BatchV1Api
};