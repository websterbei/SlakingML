<template>
    <v-col>
      <span>return statement:{{returnstatement}}</span>
      <v-list v-for="job in job_list" :key='job.job_id'>
         <v-card
            class="mx-auto"
            outlined
          >
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">{{job.name}}</v-list-item-title>
              <v-list-item-subtitle>job ID: {{job.job_id}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
      
          <v-card-actions>
            <span>Status: {{job.status}}</span>
            <v-btn color='blue' text>View Details</v-btn>
            <v-btn color='green' text>Deploy</v-btn>
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
},
  computed: {
},
created(){
  this.$http.get('http://localhost:8083/jobs').then(function(data){
    this.job_id_list = data.jobs;
    this.returnstatement = data;
  });

  var job_id;
  for(job_id of this.job_id_list){
    this.$http.get('http://localhost:8083/jobs/'+job_id).then(function(data){
    this.job_list.push({
      job_id: data.job_id,
      name: data.name,
      status: data.status,
      data_location: data.data_location,
      model_location: data.model_location,
      training_result_location: data.training_result_location
    });
    });
  }
  
}
}
</script>


<style>
</style>
