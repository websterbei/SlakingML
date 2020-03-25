<template>
  <div class="drag-drop" ref="drag-drop">
    <p>{{message}}</p>
    <h2>Drag And Drop</h2>
    <v-col>
      <v-row>
        <v-col class="d-flex" cols="12" sm="6" style="padding-bottom: 0px; height: 82px">
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
      pytorch_code: "placeholder",
      modelParameters: {
        optimizer: "adam",
        learning_rate: "0.0001",
        loss_func: "CrossEntropyLoss",
        input_size: "10",
        output_size: "10"
      },
      newBlock: "",
      newBlockParams: {
        in: 0,
        out: 0
      },
      blockTypes: ["input", "linear", "add", "concat", "output"],
      blockParams: {
        linear: ["in", "out"],
        add: [],
        concat: [],
        input: ["in"],
        output: ["out"]
      },
      nextid: "3",
      chart_data: {
        centerX: 1024,
        centerY: 140,
        scale: 1,
        nodes: [
          {
            id: "1",
            label: "",
            type: "input",
            x: -780,
            y: -120
          },
          {
            id: "2",
            label: "",
            type: "output",
            x: -780,
            y: 550
          },
          {
            id: "3",
            label: "fortesting",
            type: "linear",
            x: -780,
            y: 250,
            parameters: {
              in: 0,
              out: 0
            }
          }
        ],
        links: [
          {
            id: 0,
            from: "1",
            to: "3"
          },
          {
            id: 1,
            from: "3",
            to: "2"
          }
        ]
      }
    };
  },
  components: {
    SimpleFlowchart
  },
  methods: {
    addBlock: function() {
      var labelstring = "";
      var param = "";
      for (param in this.blockParams[this.newBlock]) {
        labelstring =
          labelstring +
          this.blockParams[this.newBlock][param] +
          ":" +
          this.newBlockParams[this.blockParams[this.newBlock][param]] +
          ", ";
      }
      this.chart_data.nodes.push({
        id: this.nextid,
        x: -1000,
        y: -100,
        type: this.newBlock,
        label: labelstring,
        parameters: this.newBlockParams
      });
      var next = parseInt(this.nextid) + 1;
      this.nextid = next.toString;
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