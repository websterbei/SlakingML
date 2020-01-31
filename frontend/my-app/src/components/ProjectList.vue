<template>
    <v-col>
      <!-- <span>FOR DEBUG: return statement:{{returnstatement}}</span> -->
      <v-btn v-on:click.prevent="refresh">Refresh</v-btn>
      <v-list v-for="job in job_list" :key='job.job_id'>
         <v-card
            class="mx-auto"
            outlined
          >
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">{{job.model_name}}</v-list-item-title>
              <v-list-item-subtitle>Job ID: {{job.job_id}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
      
          <v-card-actions>
              <router-link :to="{ name: 'ProjectDetail', params: { id:job.job_id } }" tag="v-btn">
                <v-btn color='blue' text>View Details</v-btn>
              </router-link>
              <router-link :to="{ name: 'deployid', params: { id:job.job_id } }" tag="v-btn">
                <v-btn color='green' text>Deploy</v-btn>
              </router-link>
              <v-btn v-on:click.prevent="deleteJob(job.job_id)" color='red' text>Delete</v-btn>
          </v-card-actions>
       </v-card>
      </v-list>
      
    </v-col>
</template>

<script>
export default {
  data() {
    return {
      job_id_list:[],
      job_list:[],
      returnstatement:""
      }
  },
  methods: {
    refresh: function(){
      this.job_id_list = [];
      this.job_list = [];
      var id;
      this.$http
        .get('http://localhost:8082/jobs')
        .then((response)=>{
          this.job_id_list = response.data.jobs
          for(id of this.job_id_list){
              this.$http
                .get('http://localhost:8082/jobs/'+id)
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
            }
        }
        );
    },
    deleteJob: function(id){
      this.$http
      .delete('http://localhost:8082/jobs/'+id)
      .then((response)=>{
        if(!response.data.status==="successful"){
          this.returnstatement = response
        }
      })
      this.job_id_list = [];
      this.job_list = [];
      this.$http
        .get('http://localhost:8082/jobs')
        .then((response)=>{
          this.job_id_list = response.data.jobs
          for(id of this.job_id_list){
              this.$http
                .get('http://localhost:8082/jobs/'+id)
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
            }
        }
        );
    }
  },
     
  computed: {},
  created(){
      var id;
      this.$http
        .get('http://localhost:8082/jobs')
        .then((response)=>{
          this.job_id_list = response.data.jobs
          for(id of this.job_id_list){
              this.$http
                .get('http://localhost:8082/jobs/'+id)
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
            }
        }
        );
  }
}
</script>


<style>
</style>