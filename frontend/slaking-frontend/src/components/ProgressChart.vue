<template>
  <div class="ProgressChart" ref="ProgressChart">
    <chart :chart-data="datacollection" :height='height' :max-width="auto"></chart>
  </div>
</template>

<script>
// const gradients = [
//     ['#222'],
//     ['#42b3f4'],
//     ['red', 'orange', 'yellow'],
//     ['purple', 'violet'],
//     ['#00c6ff', '#F0F', '#FF0'],
//     ['#f72047', '#ffd200', '#1feaea'],
//   ]
// import PrismEditor from "vue-prism-editor";
import Chart from "@/plugins/Chart.js";

export default {
  name: "ProgressChart",
  props: {
    datapoints: [],
    title: String
  },
  data() {
    return {
      datacollection: null,
      height: 100,
      width: 500
    };
  },
  components: {
    // PrismEditor,
    Chart
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
            backgroundColor: 'lightblue',
            borderColor: 'lightblue',
            fill: false,
            data: this.datapoints
          }
        ]
      };
    }
  }
};
</script>

