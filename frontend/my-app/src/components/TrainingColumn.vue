<template>
    <v-col class = 'text-center'>
      <p>Job ID: {{JobID}},  Version Number: {{VersionNum}}</p>
      <v-text-field
      label="Project Name"
      placeholder="MyProject"
      ></v-text-field>
    
      <v-text-field
      label="Author(s)"
      placeholder="author"
      ></v-text-field>


      <v-file-input show-size label="Model input"></v-file-input>

      <v-file-input show-size label="Data input"></v-file-input>

      <v-btn> Start Training </v-btn>
    </v-col>
</template>

<script>
export default {
  data() {
    return {
      JobID: '001',
      VersionNum: '001'
    }
  },
  methods: {
},
  computed: {
},
}
</script>


<style>
</style>
