<!--
  @Author: Webster Bei Yijie, Joey Junyu Liang
  @Date: 5/8/2020, 3:11:27 PM
  @Email: yijie.bei@duke.edu, junyu.liang@duke.edu
-->


<template>
  <v-col md="8">
    <v-col padding-bottom>
      <p>Job ID: {{job.job_id}}</p>
    </v-col>
    <v-text-field
      label="Project Name"
      placeholder="MyProject"
      v-model="job.model_name"
      required
      outlined
    ></v-text-field>

    <v-text-field
      label="Author(s)"
      placeholder="author"
      v-model="job.author_name"
      required
      outlined
    ></v-text-field>

    <h4>Enter your training model class in the below box:</h4>
    <prism-editor
      label="Training Model"
      v-model="job.model_config"
      language="js"
      :line-numbers="true"
    />
    <h4>Enter your data configuration metadata in the below box:</h4>
    <prism-editor label="Data Config" v-model="job.data_config" language="js" line-numbers="true" />
    
    <h4>Additional training configuration options:</h4>
    <br>
    <br>
    <v-slider
        v-model="job.training_config.num_trainer"
        min="1"
        max="8"
        label="Number of Trainers"
        thumb-label="always"
      ></v-slider>

    <v-btn v-on:click.prevent="post">Start Training</v-btn>
  </v-col>
</template>

<script>
import PrismEditor from "vue-prism-editor";
// import "prismjs/themes/prism.css";
import "./prism-theme.css";
import "./prism_editor.css";
import { backendAddress } from "@/configurations.js";
export default {
  data() {
    return {
      job: {
        job_id: "",
        model_name: "",
        author_name: "",
        // status:"",
        data_config:
          '{\n\t"train_dataset_path": "fashion_mnist", \n\t"test_dataset_path": "fashion_mnist", \n\t"epochs": 2,\n\t"batch_size": 20\n}',
        model_config:
          "class Model():\n" +
          '    optimizer = "adam"  // CHANGE THIS\n' +
          "    learning_rate = 0.0001 //CHANGE THIS\n" +
          "    \n" +
          "    # initialize method is called once before forward and loss methods are called\n" +
          "    def initialize(self):\n" +
          "        // YOUR CODE HERE\n" +
          "\n" +
          "    # y_: label\n" +
          "    # y: model output from forward method\n" +
          "    def loss(self, y_, y):\n" +
          "        // YOUR CODE HERE\n" +
          "\n" +
          "    def forward(self, x):\n" +
          "        // YOUR CODE HERE",
        training_config: {num_trainer: 1}
      },
      job_added_status: ""
    };
  },
  methods: {
    post: function() {
      this.$http
        .post(backendAddress + "jobs", {
          model_name: this.job.model_name,
          author_name: this.job.author_name,
          model_config: this.job.model_config,
          data_config: this.job.data_config,
          training_config: this.job.training_config
        })
        .then(response => (this.job.job_id = response.data.job_id));
    }
  },
  computed: {},
  components: {
    PrismEditor
  }
};
</script>


<style>
</style>
