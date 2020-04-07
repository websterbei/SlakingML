<template>
  <div class="codebuilder" ref="codebuilder">
    <h1>Dagger</h1>
    <h3>Your no-code pytorch model builder</h3>
    <DragAndDrop></DragAndDrop>
  </div>
</template>


<script>
import DragAndDrop from "@/components/DragAndDrop"
export default {
  data() {
  },
  components: {
    DragAndDrop
  },
  methods: {}
};
</script>

<style>
.my-editor {
  height: 300px;
}
</style>