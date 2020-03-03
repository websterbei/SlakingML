<template>
  <div class="deploylist" ref="deploylist">
    <v-col>
      <v-row>
        <h1 justify-start>Deployed Models</h1>
        <v-row justify="end">
          <v-btn fab dark color="cyan" v-on:click.prevent="refresh">
            <v-icon dark>mdi-refresh</v-icon>
          </v-btn>
        </v-row>
      </v-row>
      <p></p>
<!-- 
      <v-layout wrap>
        <v-flex pa-3 md12 v-for="job in complete_list" :key="job.job_id">
          <v-row>
            <v-card outlined>Job ID: {{job.job_id}}</v-card>
            <v-card outlined>Model Name: {{job.model_name}}</v-card>
            <v-card outlined>Endpoint: {{job.endpoint}}</v-card>
            <v-btn v-on:click.prevent="deleteDeployment(job.job_id)" color="red" text>Terminate</v-btn>
          </v-row>
        </v-flex>
      </v-layout> -->




      <v-card>
      <v-card-title>
        Showing currently available deployments
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
      </v-card-title>


      <v-data-table
        :headers="headers"
        :items="complete_list"
        class="elevation-1"
        :search="search"
      >
      <template v-slot:items="item">
          <tr>
          <td>{{ item.model_name }}</td>
          <td class="text-xs-right">{{ item.job_id }}</td>
          <td class="text-xs-right">{{ item.endpoint }}</td>
          <td>
            <v-btn v-on:click.prevent="deleteDeployment(job.job_id)" color="red" text>Terminate</v-btn>  
          </td>
          </tr>
        </template>
        <template v-slot:no-results>
          <v-alert :value="true" color="error" icon="warning">
            Your search for "{{ search }}" found no results.
          </v-alert>
        </template>
      </v-data-table>


      </v-card>
    </v-col>




  </div>
</template>

<script>
import {backendAddress} from '@/configurations.js'
export default {
  data() {
    return {
      complete_list:[],
      search: '',
      headers: [
        {
          text: 'Model Name',
          align: 'left',
          value: 'model_name'
        },
        { text: 'Job ID', value: 'job_id' },
        { text: 'Endpoint', value: 'endpoint' },
        { text: 'Actions', value: '', sortable: false }
      ],
      }
  },
  methods: {
    refresh: function(){
      var job;
      this.complete_list = [];
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
    },
    deleteItem: function(job){
      this.$http
      .delete(backendAddress + 'deployments/'+job.job_id)
      .then((response)=>{
        if(!response.data.status==="successful"){
          this.returnstatement = response
        }
      });
      var tmpjob;
      this.complete_list = [];
      this.$http
        .get(backendAddress + 'deployments')
        .then((response)=>{
          for(tmpjob of response.data){
              this.$http
                .get(backendAddress + 'jobs/'+tmpjob.job_id)
                .then((response)=>{
                  this.complete_list.push(
                    {
                      job_id:tmpjob.job_id,
                      model_name:response.data.model_name,
                      endpoint:tmpjob.endpoint
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
      this.complete_list = [];
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