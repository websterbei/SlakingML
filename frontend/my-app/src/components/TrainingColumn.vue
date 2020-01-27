<template>
    <v-col class="text-center">
            <h2>Training</h2>
            <v-col cols="12" sm="6" md="3" class="text-center">
            <v-row>
                <v-text-field
                label="Project Name"
                placeholder="MyProject"
                ></v-text-field>
                
                <v-text-field
                label="Author(s)"
                placeholder="author"
                ></v-text-field>
                <p>Job ID: {{JobID}}, Version Number: {{VersionNum}}</p>
            </v-row>
            </v-col>
            <v-row>
            <v-file-input show-size label="Model input"></v-file-input>
            <v-file-input show-size label="Data input"></v-file-input>
            </v-row>
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
