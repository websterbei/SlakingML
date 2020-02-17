<template>

    <v-col>
        <v-row>
            <v-menu offset-y>
                <template v-slot:activator="{ on }">
                    <v-btn
                    color="primary"
                    dark
                    v-on="on"
                    >
                    Select a model to deploy
                    </v-btn>
                </template>
                <v-list>
                    <v-list-item
                    v-for="id in job_id_list"
                    :key="id"
                    :value="id"
                    @click="selectproject(id)"
                    >
                    <v-list-item-title>{{ id }}</v-list-item-title>
                    </v-list-item>
                </v-list>
            </v-menu>
        </v-row>
        <p>Job ID: {{job.job_id}}</p>
        <p>Model name: {{job.model_name}}</p>
        <p>Author name: {{job.author_name}}</p>
        <p>Model Configuration: {{job.model_config}}</p>
        <p>Data Configuration: {{job.data_config}}</p>
        <v-row>
        <v-btn>TODO: Deploy</v-btn>
        </v-row>
        <v-row>
        <v-btn v-on:click.prevent="refresh">Refresh</v-btn>
        </v-row>

    </v-col>
</template>

<script>
import {backendAddress} from '@/configurations.js'
export default {
  data() {
    return {
      job_id_list:[],
      job:{
        job_id:"",
        model_name:"",
        author_name:"",
        // status:"",
        data_config:"",
        model_config:"",
        // training_result_config:""
      }
  }},
  methods: {
    refresh: function(){
      this.$http
        .get(backendAddress + 'jobs')
        .then((response)=>this.job_id_list = response.data.jobs)
      this.$http
                .get(backendAddress + 'jobs/'+this.job.job_id)
                .then((response)=>{
                  this.job_list.push(
                    {
                      job_id:response.data.job_id,
                      data_config:response.data.data_config,
                      model_config: response.data.model_config,
                      model_name:response.data.model_name,
                      author_name:response.data.author_name
                    }
                  )
                });
    },
    selectproject: function(id){
      this.job.job_id = id;
      this.$http
                .get(backendAddress + 'jobs/'+id)
                .then((response)=>{
                    this.job.job_id=response.data.job_id;
                    this.job.data_config=response.data.data_config;
                    this.job.model_config= response.data.model_config;
                    this.job.model_name=response.data.model_name;
                    this.job.author_name=response.data.author_name;

                });
    }
  },
     
  computed: {},
  created(){
      this.job.job_id=this.$route.params.id;
      this.$http
        .get(backendAddress + 'jobs')
        .then((response)=>this.job_id_list = response.data.jobs)
      this.$http
                .get(backendAddress + 'jobs/'+this.job.job_id)
                .then((response)=>{
                    this.job.job_id=response.data.job_id;
                    this.job.data_config=response.data.data_config;
                    this.job.model_config= response.data.model_config;
                    this.job.model_name=response.data.model_name;
                    this.job.author_name=response.data.author_name;
                });
  }
}
</script>


<style>
</style>