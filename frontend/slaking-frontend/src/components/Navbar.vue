<template>
<div class="Navbar">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list dense>
        <router-link to='/' tag='v-list-item'>
            <v-list-item link>
                <v-list-item-action>
                    <v-icon>mdi-home</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title>Home</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </router-link>

        <router-link to='/training' tag='v-list-item'>
            <v-list-item link>
                <v-list-item-action>
                    <v-icon>mdi-cloud-upload</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title>New Training</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </router-link>

        <router-link to='/progress' tag='v-list-item'>
            <v-list-item link>
                <v-list-item-action>
                    <v-icon>mdi-view-list</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title>Projects List</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </router-link>

        <router-link to='/deploy' tag='v-list-item'>
            <v-list-item link>
                <v-list-item-action>
                    <v-icon>mdi-shovel</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title>Deploy Model</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </router-link>

        <router-link to='/about' tag='v-list-item'>
            <v-list-item link>
                <v-list-item-action>
                    <v-icon>mdi-information</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                    <v-list-item-title>About</v-list-item-title>
                </v-list-item-content>
            </v-list-item>
        </router-link>
 
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>
        Slaking
        <span class="font-weight-thin"> - ML suite built for small to medium businesses
 </span>
      </v-toolbar-title>
    </v-app-bar>
</div>
</template>

<script>
export default {
    data: () => ({
      drawer: null,
    })
}
</script>