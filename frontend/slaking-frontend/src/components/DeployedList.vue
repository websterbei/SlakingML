<template>
<div class="deploylist" ref="deploylist">
    <v-col>
      <v-row>
        <h1 justify-start>Deployed Models</h1>
      <v-row justify="end">
        <v-btn fab small dark color="cyan" v-on:click.prevent="refresh">
          <v-icon  dark>mdi-refresh</v-icon>
        </v-btn>
      </v-row>
      </v-row>
      <p> </p>

   <v-layout wrap>
       <v-flex pa-3 md12 v-for="job in complete_list" :key='job.job_id'>
            <v-row>
                <v-card outlined>Job ID: {{job.job_id}}</v-card>
                <v-card outlined>Model Name: {{job.model_name}}</v-card>
                <v-card outlined>Endpoint: {{job.endpoint}}</v-card>
            </v-row>
       </v-flex>
   </v-layout>
      
    </v-col>
</div>
</template>

<script>
import {backendAddress} from '@/configurations.js'
export default {
  data() {
    return {
      complete_list:[]
      }
  },
  methods: {
    refresh: function(){
      var job;
      this.$http
        .get(backendAddress + 'deployments')
        .then((response)=>{
          for(job of response.data){
              this.$http
                .get(backendAddress + 'jobs/'+job.job_id)
                .then((response)=>{
                  this.complete_list.push(
                    {
                      job_id:job.job_id,
                      model_name:response.data.model_name,
                      endpoint:job.endpoint
                    }
                  )
                });
            }
        }
        );
    }
  },
     
  computed: {},
  created(){
      var job;
      this.$http
        .get(backendAddress + 'deployments')
        .then((response)=>{
          for(job of response.data){
              this.$http
                .get(backendAddress + 'jobs/'+job.job_id)
                .then((response)=>{
                  this.complete_list.push(
                    {
                      job_id:job.job_id,
                      model_name:response.data.model_name,
                      endpoint:job.endpoint
                    }
                  )
                });
            }
        }
        );
  }
}
</script>


<style>
</style>