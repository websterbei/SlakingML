<template>
    <v-col>
      <!-- <span>FOR DEBUG: return statement:{{returnstatement}}{{job_id_list}}</span> -->
      <v-btn v-on:click.prevent="refresh">Refresh</v-btn>
      <v-list v-for="job in job_list" :key='job.job_id'>
         <v-card
            class="mx-auto"
            outlined
          >
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">{{job.model_name}}</v-list-item-title>
              <v-list-item-subtitle>job ID: {{job.job_id}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
      
          <v-card-actions>
            <!-- <span>Status: {{job.status}}</span> -->
            <v-btn color='blue' text>View Details</v-btn>
            <v-btn color='green' text>Deploy</v-btn>
            <v-btn color='red' text>Delete</v-btn>
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
      // var idlist = [];
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