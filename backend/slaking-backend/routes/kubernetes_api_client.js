const k8s = require('@kubernetes/client-node');

const kc = new k8s.KubeConfig();
kc.loadFromFile('./routes/kubernetes_config.yml');
const k8sApi = kc.makeApiClient(k8s.CoreV1Api);

module.exports = k8sApi;