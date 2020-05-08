<!--
  @Author: Webster Bei Yijie, Joey Junyu Liang
  @Date: 5/8/2020, 3:24:28 PM
  @Email: yijie.bei@duke.edu, junyu.liang@duke.edu
-->


<template>
  <div class="about" ref="about">
    <h2>Slaking ML</h2>
    <h4>--a scalable machine learning pipeline on Kubernetes</h4>
    <p>{{authors}}</p>
  </div>
</template>


<script>
export default {
  data() {
    return {
      authors:
        "\n\n\n      Authors:\n      Joey Junyu Liang\n      Webster Bei Yijie"
    };
  },
  components: {},
  methods: {}
};
</script>
