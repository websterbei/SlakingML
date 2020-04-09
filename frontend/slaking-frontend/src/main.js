import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import axios from "axios";

Vue.prototype.$http = axios;
Vue.config.productionTip = false;

import "prismjs";
import VuePrismEditor from "vue-prism-editor";
import vuechartjs from "vue-chartjs";
import VuePrism from "vue-prism";
// import SimpleFlowchart from 'vue-simple-flowchart';
// import 'vue-simple-flowchart/dist/vue-flowchart.css';
Vue.use(VuePrism);
Vue.use(vuetify);
Vue.use(vuechartjs);
Vue.component("prism-editor", VuePrismEditor);

new Vue({
  router,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
