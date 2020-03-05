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
      <template v-slot:item.actions="{ item }">
            <v-chip color="red" dark v-on:click.prevent="deleteDeployment(item.job_id)">Terminate</v-chip>
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
        { text: 'Actions', value: 'actions', sortable: false }
      ],
      }
  },
  methods: {
    refresh: function(){
      this.complete_list = [];
      this.$http
        .get(backendAddress + 'deployments')
        .then((response)=>{
          this.complete_list = response.data;
        }
        );
    },
    deleteDeployment: function(job_id){
      this.$http
      .delete(backendAddress + 'deployments/'+job_id)
      .then((response)=>{
        if(!response.data.status==="successful"){
          this.returnstatement = response;
        }
      });
      this.complete_list = [];
      this.$http
        .get(backendAddress + 'deployments')
        .then((response)=>{
          this.complete_list = response.data;
        }
        );
    }
      
  },
     
  computed: {},
  created(){
      this.complete_list = [];
      this.$http
        .get(backendAddress + 'deployments')
        .then((response)=>{
          this.complete_list = response.data;
        }
        );
  }
}
</script>


<style>
</style>