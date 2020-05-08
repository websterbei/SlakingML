<!--
  @Author: Webster Bei Yijie, Joey Junyu Liang
  @Date: 5/8/2020, 3:11:24 PM
  @Email: yijie.bei@duke.edu, junyu.liang@duke.edu
-->


<template>
  <div class="projectlist" ref="projectlist">
    <v-col>
      <v-row>
        <h1 justify-start>Models List</h1>
        <v-row justify="end">
          <v-btn fab dark color="cyan" v-on:click.prevent="refresh">
            <v-icon large dark>mdi-refresh</v-icon>
          </v-btn>
        </v-row>
      </v-row>
      <p></p>

      <v-layout wrap>
        <v-flex pa-3 md5 v-for="job in job_list" :key="job.job_id">
          <v-card outlined hover>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title class="headline mb-1">{{job.model_name}}</v-list-item-title>
                <v-list-item-subtitle>Job ID: {{job.job_id}}</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-card-actions>
              <router-link :to="{ name: 'ProjectDetail', params: { id:job.job_id } }" tag="v-btn">
                <v-btn color="blue" text>View Details</v-btn>
              </router-link>
              <router-link :to="{ name: 'deployid', params: { id:job.job_id } }" tag="v-btn">
                <v-btn color="green" v-on:click.prevent="deployJob(job.job_id)" text>Deploy</v-btn>
              </router-link>
              <v-btn v-on:click.prevent="deleteJob(job.job_id)" color="red" text>Delete</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-col>
  </div>
</template>

<script>
import { backendAddress } from "@/configurations.js";
export default {
  data() {
    return {
      job_id_list: [],
      job_list: [],
      returnstatement: "",
      deploy_returnstatement: ""
    };
  },
  methods: {
    refresh: function() {
      this.job_list = [];
      this.$http.get(backendAddress + "jobs?details=true").then(response => {
        this.job_list = response.data.jobs;
      });
    },
    deleteJob: function(id) {
      this.$http.delete(backendAddress + "jobs/" + id).then(response => {
        if (!response.data.status === "successful") {
          this.returnstatement = response;
        }
      });
      this.job_list = [];
      this.$http.get(backendAddress + "jobs?details=true").then(response => {
        this.job_list = response.data.jobs;
      });
    },
    deployJob: function(id) {
      this.$http.put(backendAddress + "deployments/" + id).then(response => {
        this.deploy_returnstatement = response;
      });
    }
  },

  computed: {},
  created() {
    this.$http.get(backendAddress + "jobs?details=true").then(response => {
      this.job_list = response.data.jobs;
    });
  }
};
</script>


<style>
</style>