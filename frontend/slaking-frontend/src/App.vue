<template>
  <v-app id="app">
    <Navbar></Navbar>
    <v-content align="start">
      <v-container fluid align="start">
        <v-col align-items="start" align="start">
        <router-view align="start"></router-view>
        </v-col>
      </v-container>
    </v-content>
    <v-footer
      color="indigo"
      app
    >
      <span class="white--text">&copy; 2020</span>
    </v-footer>
  </v-app>
</template>




<script>
import Navbar from '@/components/Navbar'
  export default {
    props: {
      source: String,
    },
    components:{ Navbar},
    data: () => ({
      drawer: null
    }),
  }
</script>




