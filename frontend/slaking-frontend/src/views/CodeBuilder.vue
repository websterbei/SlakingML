<!--
  @Author: Webster Bei Yijie, Joey Junyu Liang
  @Date: 5/8/2020, 3:24:30 PM
  @Email: yijie.bei@duke.edu, junyu.liang@duke.edu
-->


<template>
  <div class="codebuilder" ref="codebuilder">
    <h1>Dagger</h1>
    <h3>Your no-code pytorch model builder</h3>
    <DragAndDrop></DragAndDrop>
  </div>
</template>


<script>
import DragAndDrop from "@/components/DragAndDrop";
export default {
  components: {
    DragAndDrop
  }
};
</script>

