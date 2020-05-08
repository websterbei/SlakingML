<!--
  @Author: Webster Bei Yijie, Joey Junyu Liang
  @Date: 5/8/2020, 3:24:34 PM
  @Email: yijie.bei@duke.edu, junyu.liang@duke.edu
-->


<template>
  <div class="home">
    <v-container justify-start>
      <h1 pa-4 ma-4>Welcome to Slaking!</h1>
      <HomeFlowChart></HomeFlowChart>
    </v-container>
  </div>
</template>

<script>
import HomeFlowChart from "@/components/HomeFlowChart.vue";
export default {
  components: {
    HomeFlowChart
  }
};
</script>