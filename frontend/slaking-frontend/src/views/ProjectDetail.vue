<template>
  <div class="projectdetail">
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
