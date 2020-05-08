<!--
  @Author: Webster Bei Yijie, Joey Junyu Liang
  @Date: 5/8/2020, 3:11:16 PM
  @Email: yijie.bei@duke.edu, junyu.liang@duke.edu
-->


<template>
  <v-col class="text-center">
    <h3>Training Progress</h3>
    <v-list v-for="metric in metrics" :key="metric">
      <ProgressChart :title="metric" :datapoints="values[metric]"></ProgressChart>
    </v-list>
  </v-col>
</template>

<script>
import { backendAddress } from "@/configurations.js";
import ProgressChart from "@/components/ProgressChart.vue";

export default {
  components: {
    ProgressChart
  },
  data: () => ({
    metrics: [],
    values: []
  }),
  created() {
    var job_id = this.$route.params.id;
    this.$http.get(backendAddress + "jobs/" + job_id).then(response => {
      this.values = response.data.metrics;
      for (var key in response.data.metrics) {
        this.metrics.push(key);
      }
    });
  }
};
</script>

