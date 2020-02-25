<template>
  <div class="about" ref="about">
    <h2>Testing page</h2>
    <!-- <h3>Project Vision</h3> -->
    <!-- <span>Our team aims to build a ML-as-a-service platform, targeting users ranging from individuals to small to medium size business. The product will cover the end-to-end ML workflow, including data management, training, and deployment. With this product, users should be able to train and deploy machine learning models without worrying about allocating storage/computing resources, or setting up workflows.</span> --> -->
    <!-- <prism-editor min-width = "200px" v-model="code" language="js" :line-numbers="lineNumbers" class="my-editor" /> -->
    <!-- <Line
      :data="dataset"
      :bind="true"
      :labels="labels"
    />     -->
    <chart :chart-data="datacollection"></chart>
  </div>
</template>

<script>
// import PrismEditor from "vue-prism-editor";
import Chart from "../components/Chart.js"

export default {
  data() {
        return {
            datacollection: null
        }
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
          this.datacollection = {
            labels: [
              "January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December"
            ],
            datasets: [
              {
                label: "GitHub Commits",
                backgroundColor: "#f87979",
                data: [70, 20, 12, 39, 100, 40, 95, 80, 80, 20, 12, 101]
              },
              {
                label: "Monthly incomes",
                backgroundColor: "#A5CC82",
                data: [205, 408, 188, 190, 58, 200, 190, 400, 164, 254, 290, 201]
              }
            ]
          };
        },
      }
};

</script>

<style>
.my-editor{
  height: 300px;
}
</style>