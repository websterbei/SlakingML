<!--
  @Author: Webster Bei Yijie, Joey Junyu Liang
  @Date: 5/8/2020, 3:11:05 PM
  @Email: yijie.bei@duke.edu, junyu.liang@duke.edu
-->


<template>
  <div name="HomeFlowChart">
    <v-container md6 justify="start">
      <v-col>
        <v-timeline align-top>
          <v-timeline-item
            v-for="(item, i) in items"
            :key="i"
            :color="item.color"
            :icon="item.icon"
            fill-dot
          >
            <router-link :to="item.link" tag="v-card">
              <v-card hover :color="item.color" dark>
                <v-card-title class="title">{{item.title}}</v-card-title>
                <v-card-text class="white text--primary pa-4">
                  <p pa-2 ma-2>{{item.description}}</p>
                  <!-- <v-btn :color="item.color" class="mx-0" outlined>Button</v-btn> -->
                </v-card-text>
              </v-card>
            </router-link>
          </v-timeline-item>
        </v-timeline>
      </v-col>
    </v-container>
  </div>
</template>

<script>
// import { backendAddress } from "@/configurations.js";

export default {
  components: {},
  data: () => ({
    items: [
      {
        color: "red lighten-2",
        icon: "mdi-plus",
        title: "Create New Training Model",
        description: "Click to create a new training model",
        link: "/training"
      },
      {
        color: "purple darken-1",
        icon: "mdi-library",
        title: "View exisitng models",
        description:
          "Click to view information and status for previously added training models. Choose project to deploy if needed.",
        link: "/progress"
      },
      {
        color: "green lighten-1",
        icon: "mdi-shovel",
        title: "View Deployed Models",
        description:
          "Click to get a list of deployed models and their endpoints.",
        link: "/deploy"
      },
      {
        color: "orange lighten-1",
        icon: "mdi-sitemap",
        title: "Dagger",
        description: "Click to construct your PyTorch model using our no-code builder",
        link: "/codebuilder"
      },
      {
        color: "indigo",
        icon: "mdi-information",
        title: "Info and Documentation",
        description: "Click to get instructions and documentation",
        link: "/about"
      }
    ]
  }),
  created() {}
};
</script>

