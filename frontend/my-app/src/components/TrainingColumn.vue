<template>
    <v-col class = 'text-center'>
      <p>Job ID: {{JobID}},  Version Number: {{VersionNum}}</p>
      <v-text-field
      label="Project Name"
      placeholder="MyProject"
      ></v-text-field>
    
      <!-- <v-text-field
      label="Author(s)"
      placeholder="author"
      ></v-text-field> -->


      <v-file-input show-size label="Model input"></v-file-input>

      <v-file-input show-size label="Data input"></v-file-input>
      <v-btn v-on:click.prevent="post">Add Project</v-btn>
      <v-btn> Start Training </v-btn>
    </v-col>
</template>

<script>
export default {
  data() {
    return {
      job:{
        job_id:"",
        name:"",
        status:"",
        data_location:"",
        model_location:"",
        training_result_location:""
      },
      job_added_status :""
    }
  },
  methods: {
    post: function(){
            this.$http.post('http://8083/jobs', {
                job_id: this.job.job_id,
                name: this.job.name,
                status: this.job.status,
                data_location: this.job.data_location,
                model_location: this.job.model_location,
                training_result_location: this.job.training_result_location
            }).then(function(status){
                this.job_added_status = status;
            });
        }
},
  computed: {
},
}
</script>


<style>
</style>
