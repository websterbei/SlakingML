<template>
    <v-col>
      <!-- <p>FOR DEBUG: return statement: {{job_added_status}}  model:{{job.model_config}} {{job.name}}</p> -->
      <p>Job ID: {{job.job_id}}</p>
      <!-- <p> Number: {{VersionNum}}</p> -->
      <v-text-field
      label="Project Name"
      placeholder="MyProject"
      v-model="job.name"
      required
      ></v-text-field>
    
      <v-text-field
      label="Author(s)"
      placeholder="author"
      v-model="job.author"
      required
      ></v-text-field>

      <v-text-field
      label="Model File Path"
      placeholder=""
      v-model="job.model_config"
      required
      ></v-text-field>

      <v-text-field
      label="Data File Path"
      placeholder=""
      v-model="job.data_config"
      required
      ></v-text-field>

      <!-- <v-file-input show-size label="Model Config" v-model="model_file"></v-file-input> -->
      <!-- <v-file-input show-size label="Data Config"></v-file-input> -->
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
        author:"",
        status:"",
        data_config:"",
        model_config:"",
        training_result_config:""
      },
      job_added_status :"",
    }
  },
  methods: {
    post: function(){
            this.$http.post('http://localhost:8082/jobs', {
                model_name: this.job.name,
                author_name: this.job.author,
                model_config: this.job.model_config,
                data_config: this.job.data_config
            })
            .then(response => this.job.job_id = response.data.job_id);
        }
},
  computed: {
},
}
</script>


<style>
</style>
