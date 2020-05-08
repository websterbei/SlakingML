<!--
  @Author: Webster Bei Yijie, Joey Junyu Liang
  @Date: 5/8/2020, 3:11:22 PM
  @Email: yijie.bei@duke.edu, junyu.liang@duke.edu
-->


<template>
  <v-col>
    <v-row pa-3>
      <h1>{{job.model_name}}</h1>
    </v-row>

    <v-col>
      <h3>Job ID:</h3>
      <p>{{job.job_id}}</p>
      <!-- <p>Model name: {{job.model_name}}</p> -->
      <h3>Author name:</h3>
      <p>{{job.author_name}}</p>
      <h3>Model Configuration:</h3>
      <code>{{job.model_config}}</code>
      <p></p>
      <h3>Data Configuration:</h3>
      <code>{{job.data_config}}</code>
    </v-col>
  </v-col>
</template>

<script>
import { backendAddress } from "@/configurations.js";
export default {
  data() {
    return {
      job_id_list: [],
      job: {
        job_id: "",
        model_name: "",
        author_name: "",
        data_config: "",
        model_config: ""
      }
    };
  },
  methods: {},

  computed: {},
  created() {
    this.job.job_id = this.$route.params.id;
    this.$http
      .get(backendAddress + "jobs")
      .then(response => (this.job_id_list = response.data.jobs));
    this.$http
      .get(backendAddress + "jobs/" + this.job.job_id)
      .then(response => {
        this.job.job_id = response.data.job_id;
        this.job.data_config = response.data.data_config;
        this.job.model_config = response.data.model_config;
        this.job.model_name = response.data.model_name;
        this.job.author_name = response.data.author_name;
      });
  }
};
</script>


<style>
</style>