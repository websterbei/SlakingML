<template>
    <v-col>
      <v-list v-for="task in TaskList" :key='task.taskid'>
         <v-card
            class="mx-auto"
            outlined
          >
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="headline mb-1">{{task.name}}</v-list-item-title>
              <v-list-item-subtitle>task ID: {{task.taskid}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
      
          <v-card-actions>
            <span>Status: {{task.status}}</span>
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
      TaskList:[{name:'Webster\'s project',taskid:'001', status:'ready'}, {name:'Joey\'s project',taskid:'002',status:'training'}]
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
