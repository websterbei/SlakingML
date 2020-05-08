<!--
  @Author: Webster Bei Yijie, Joey Junyu Liang
  @Date: 5/8/2020, 3:11:02 PM
  @Email: yijie.bei@duke.edu, junyu.liang@duke.edu
-->


<template>
  <div class="drag-drop" ref="drag-drop">
    <!-- <p>{{this.message}}</p> -->
    <v-col>
      <v-row>
        <v-col class="d-flex" style="padding-bottom: 0px; height: 82px">
          <v-select v-model="newBlock" :items="blockTypes" label="Block Type" outlined></v-select>
        </v-col>
        <v-list
          v-for="param in blockParams[newBlock]"
          v-bind:key="param"
          style="padding-bottom: 0px; height: 82px"
        >
          <v-col mr-4 style="padding-bottom: 0px; height: 82px">
            <v-text-field :label="param" v-model="newBlockParams[param]" required></v-text-field>
          </v-col>
        </v-list>
      </v-row>
      <v-row>
        <v-btn v-on:click.prevent="addBlock">Add Block</v-btn>
        <v-btn
          style="margin-left: 800px ;background-color: lavender;"
          v-on:click.prevent="createCode"
        >Generate Code</v-btn>
      </v-row>
    </v-col>

    <v-row>
      <v-col style="max-width: min-content;">
        <h4 style="padding-all: 3px; width: 150px">Options</h4>
        <v-text-field
          label="Optimizer"
          placeholder="adam"
          v-model="modelParameters.optimizer"
          required
        ></v-text-field>
        <v-text-field
          label="Learning Rate"
          placeholder="0.0001"
          v-model="modelParameters.learning_rate"
          required
        ></v-text-field>
        <v-text-field
          label="Loss Function Type"
          placeholder="CrossEntropyLoss"
          v-model="modelParameters.loss_func"
          required
        ></v-text-field>
        <v-text-field
          label="Input Size"
          placeholder="10"
          v-model="modelParameters.input_size"
          required
        ></v-text-field>
        <v-text-field
          label="Output Size"
          placeholder="10"
          v-model="modelParameters.output_size"
          required
        ></v-text-field>
      </v-col>
      <simple-flowchart :scene.sync="chart_data"></simple-flowchart>

      <v-col class="col" style="padding-top:0px; padding-bottom:0px">
        <code style="height:100%; width:100%">{{pytorch_code}}</code>
      </v-col>
    </v-row>
  </div>
</template>


<script>
import SimpleFlowchart from "vue-simple-flowchart";
import "./vue-flowchart.css";
import { Parser } from "@/parser/Parser";
export default {
  data() {
    return {
      message: "",
      pytorch_code: '//Press "Generate Code" to generate model code',
      modelParameters: {
        optimizer: "adam",
        learning_rate: "0.0001",
        loss_func: "CrossEntropyLoss",
        input_size: "10",
        output_size: "10"
      },
      newBlock: "",
      newBlockParams: {
        padding: 2,
        stride: "None",
        start_dim: 1,
        dimension: 2,
        in: 0,
        out: 0,
        kernel_size: 1,
        padding_mode: "zeros"
      },
      blockTypes: [
        "input",
        "Linear",
        "add",
        "concat",
        "Conv",
        "Flatten",
        "MaxPool",
        "AvgPool",
        "output"
      ],
      blockParams: {
        Linear: ["in", "out"],
        add: [],
        concat: [],
        input: ["in"],
        output: ["out"],
        Conv: [
          "dimension",
          "in",
          "out",
          "kernel_size",
          "padding",
          "stride",
          "padding_mode"
        ],
        Flatten: ["start_dim"],
        MaxPool: ["dimension", "kernel_size", "stride", "padding"],
        AvgPool: ["dimension", "kernel_size", "stride", "padding"]
      },
      nextid: 3,
      chart_data: {
        centerX: 1024,
        centerY: 140,
        scale: 1,
        nodes: [
          {
            id: 1,
            label: "id: 1",
            type: "input",
            x: -780,
            y: -120
          },
          {
            id: 2,
            label: "id: 2",
            type: "output",
            x: -780,
            y: 550
          }
        ],
        links: []
      }
    };
  },
  components: {
    SimpleFlowchart
  },
  methods: {
    addBlock: function() {
      if (this.newBlock == "") {
        return;
      }
      let in_nodes = this.newBlockParams.in;
      let out_nodes = this.newBlockParams.out;
      var labelstring = "id: " + this.nextid + ", ";
      var param = "";
      let count = 0;
      for (param in this.blockParams[this.newBlock]) {
        if (count < 3) {
          labelstring =
            labelstring +
            this.blockParams[this.newBlock][param] +
            ":" +
            this.newBlockParams[this.blockParams[this.newBlock][param]] +
            ", ";
        }
        count++;
      }
      this.chart_data.nodes.push({
        id: this.nextid,
        x: -1000,
        y: -100,
        type: this.newBlock,
        label: labelstring,
        parameters: {
          in: in_nodes,
          out: out_nodes,
          kernel_size: this.newBlockParams.kernel_size,
          padding_mode: this.newBlockParams.padding_mode,
          padding: this.newBlockParams.padding,
          stride: this.newBlockParams.stride,
          dimension: this.newBlockParams.dimension,
          start_dim: this.newBlockParams.start_dim
        }
      });
      // var next = parseInt(this.nextid) + 1;
      // let nextStr = next.toString;
      this.nextid += 1;
    },
    createCode: function() {
      var state = {
        nodes: this.chart_data.nodes,
        links: this.chart_data.links,
        modelParameters: this.modelParameters
      };
      let ret = Parser(state);
      this.pytorch_code = ret.code;
      this.message = ret;
    }
  }
};
</script>

<style>
.my-editor {
  height: 300px;
}
</style>