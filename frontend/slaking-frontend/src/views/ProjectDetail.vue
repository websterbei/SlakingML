<!--
  @Author: Webster Bei Yijie, Joey Junyu Liang
  @Date: 5/8/2020, 3:24:38 PM
  @Email: yijie.bei@duke.edu, junyu.liang@duke.edu
-->


<template>
  <div class="projectdetail">
    <v-row justify="end" class="ma-2">
      <v-tooltip bottom>
        <template v-slot:activator="{on}">
          <v-btn
            class="mr-3"
            fab
            dark
            color="green"
            v-on="on"
            v-on:click.prevent="deployJob(job_id)"
          >
            <v-icon dark>mdi-shovel</v-icon>
          </v-btn>
        </template>
        <span>Deploy Model</span>
      </v-tooltip>
      <v-tooltip bottom>
        <template v-slot:activator="{on}">
          <v-btn class="ml-3" fab dark v-on="on" color="cyan" v-on:click.prevent="forceRerender">
            <v-icon dark>mdi-refresh</v-icon>
          </v-btn>
        </template>
        <span>Refresh</span>
      </v-tooltip>
    </v-row>
    <ProjectDetailComponent :key="componentKey"></ProjectDetailComponent>
    <ProgressBar :key="componentKey"></ProgressBar>
  </div>
</template>

<script>
import { backendAddress } from "@/configurations.js";
import ProjectDetailComponent from "@/components/ProjectDetailComponent";
import ProgressBar from "@/components/ProgressBar";
export default {
  data() {
    return {
      componentKey: 0,
      job_id: ""
    };
  },
  components: { ProjectDetailComponent, ProgressBar },
  methods: {
    forceRerender() {
      this.job_id = this.$route.params.id;
      this.componentKey += 1;
    },
    deployJob: function(id) {
      console.log("deploy model: " + this.$route.params.id);
      this.$http.put(backendAddress + "deployments/" + id).then(response => {
        this.deploy_returnstatement = response;
      });
    }
  },
  created() {
    console.log(this.$route.params.id);
    this.job_id = this.$route.params.id;
  }
};
</script>
