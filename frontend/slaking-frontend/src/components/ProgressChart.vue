<template>
  <div class="ProgressChart" ref="ProgressChart">
    <chart :chart-data="datacollection" :height="height" :max-width="auto"></chart>
  </div>
</template>

<script>
import Chart from "@/plugins/Chart.js";

export default {
  data() {
    return {
      datacollection: null,
      height: 100,
      width: 500
    };
  },
  components: {
    Chart
  },
  name: "ProgressChart",
  props: {
    datapoints: [],
    title: String
  },
  mounted() {
    this.fillData();
  },
  methods: {
    fillData() {
      var label = [];
      for (var i = 1; i <= this.datapoints.length; i++) {
        label.push(i);
      }

      this.datacollection = {
        labels: label,
        datasets: [
          {
            label: this.title,
            backgroundColor: "lightblue",
            borderColor: "lightblue",
            fill: false,
            data: this.datapoints,
            pointStyle: "line",
            borderWidth: 2,
            pointRadius: 0
          }
        ]
      };
    }
  }
};
</script>

