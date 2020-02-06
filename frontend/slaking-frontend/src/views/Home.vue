<template>
  <div class="home">
    <h2>Home Page</h2>
    <v-row>
      <v-col>
        <h3>Your Recent Projects</h3>
        <ProjectList></ProjectList>
      </v-col>
      <v-col>
         <router-link to='/training' tag='v-list-item'>
            <v-list-item link>
                <v-list-item-action>
                    <v-icon>mdi-plus-box</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title>Train New Model</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </router-link>

        <router-link to='/progress' tag='v-list-item'>
            <v-list-item link>
                <v-list-item-action>
                    <v-icon>mdi-view-list</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title>View all projects</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </router-link>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import ProjectList from '@/components/ProjectList'
export default{
  components: {ProjectList}
}
</script>