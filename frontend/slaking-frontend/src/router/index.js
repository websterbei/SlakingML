/*
* @Author: Webster Bei Yijie, Joey Junyu Liang
* @Date: 5/8/2020, 3:10:49 PM
* @Email: yijie.bei@duke.edu, junyu.liang@duke.edu
*/


import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Training from '@/views/Training.vue'
import Deploy from '@/views/Deploy.vue'
import Progress from '@/views/Progress.vue'
import ProjectDetail from '@/views/ProjectDetail.vue'
import About from '@/views/About.vue'
import CodeBuilder from '@/views/CodeBuilder.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
  {
    path: '/progress',
    name: 'progress',
    component: Progress
  },
  {
    path: '/training',
    name: 'training',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: Training
  },
  {
    path: '/deploy',
    name: 'deploy',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: Deploy
  },
  // {
  //   path: '/deploy/:id',
  //   name: 'deployid',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: Deploy
  // },
  {
    path: '/projectdetail/:id',
    name: 'ProjectDetail',
    component: ProjectDetail
  },

  {
    path: '/codebuilder',
    name: 'CodeBuilder',
    component: CodeBuilder
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
