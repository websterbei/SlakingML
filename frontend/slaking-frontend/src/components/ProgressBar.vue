<template>
    <v-col class="text-center">
        <h3>Training Progress</h3>
        <v-list v-for="metric in metrics" :key='metric'>
          <v-sparkline
            :value="values[metric]"
            :gradient="gradient"
            :smooth="radius || false"
            :padding="padding"
            :line-width="width"
            :stroke-linecap="lineCap"
            :gradient-direction="gradientDirection"
            :fill="fill"
            :type="type"
            :auto-line-width="autoLineWidth"
            auto-draw
          ></v-sparkline>
        </v-list>
    </v-col>
</template>

<script>
  const gradients = [
    ['#222'],
    ['#42b3f4'],
    ['red', 'orange', 'yellow'],
    ['purple', 'violet'],
    ['#00c6ff', '#F0F', '#FF0'],
    ['#f72047', '#ffd200', '#1feaea'],
  ]

  import {backendAddress} from '@/configurations.js'

  export default {
    data: () => ({
      metrics: [],
      width: 0.5,
      radius: 10,
      padding: 8,
      lineCap: 'round',
      gradient: gradients[5],
      values: [],
      gradientDirection: 'top',
      gradients,
      fill: false,
      type: 'trend',
      autoLineWidth: false
    }),
  created() {
    var job_id=this.$route.params.id;
    this.$http
      .get(backendAddress + 'jobs/' + job_id)
      .then((response)=>{
        this.values = response.data.metrics;
        for (var key in response.data.metrics) {
          this.metrics.push(key);
        }
      });
    }
  }
</script>