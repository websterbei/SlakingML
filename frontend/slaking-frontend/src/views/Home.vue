<template>
  <div class="home" pa-4 ma-4>
      <v-container justify-start>
    <h1  pa-4 ma-4>Welcome to Slaking!</h1>
    <HomeFlowChart></HomeFlowChart>
      </v-container>
  </div>
</template>

<script>
import HomeFlowChart from '@/components/HomeFlowChart.vue'
export default{
      components: {
    HomeFlowChart
  },
}
</script>