<template>
  <div class="projectdetail">
    <h2>Project Detail</h2>
    <ProjectDetailComponent></ProjectDetailComponent>
    <ProgressBar></ProgressBar>
  </div>
</template>

<script>
import ProjectDetailComponent from '@/components/ProjectDetailComponent'
import ProgressBar from '@/components/ProgressBar'
export default{
  components: {ProjectDetailComponent,ProgressBar}
}
</script>
