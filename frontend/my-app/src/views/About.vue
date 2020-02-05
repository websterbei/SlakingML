<template>
  <div class="about">
    <!-- <h2>About</h2>
    <h3>Project Vision</h3>
    <span>Our team aims to build a ML-as-a-service platform, targeting users ranging from individuals to small to medium size business. The product will cover the end-to-end ML workflow, including data management, training, and deployment. With this product, users should be able to train and deploy machine learning models without worrying about allocating storage/computing resources, or setting up workflows.</span> -->
    <prism-editor min-width = "200px" v-model="code" language="js" :line-numbers="lineNumbers" class="my-editor" />
  </div>
</template>

<script>
import PrismEditor from "vue-prism-editor";

export default {
  data(){
    return{
      code:"// enter your code here",
      lineNumbers:true
    }
  },
  components: {
    PrismEditor
  }
};
</script>

<style>
.my-editor{
  height: 300px;
}
</style>