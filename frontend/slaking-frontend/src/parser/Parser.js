import { createGraph } from "./GraphConstructor";
import {
  GenerateInitFunctions,
  forward_linear,
  forward_add,
  forward_concat,
  forward_conv,
  forward_pool,
  forward_flatten,
} from "./Helper";

export function Parser(state) {
  if (!state.nodes.length > 0) return "";

  var params = state.modelParameters;

  // input node: id = 1
  // output node: id = 2

  /*
    params: 
    optimizer: "adam",
    learning_rate: "0.0001",
    loss_func: "CrossEntropyLoss",
    input_size: "10",
    output_size: "10"
    */

  var header = "class Model():\n";
  // "import torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom metrics import *\n\nclass Model():\n"
  var optAndRate =
    '     optimizer = "' +
    params.optimizer +
    '"\n     learning_rate = ' +
    params.learning_rate +
    "\n\n";

  var initialize_func =
    "     # initialize method is called once before \n     # forward and loss methods are called\n     def initialize(self):\n";
  var lossFn = "        self.lossFn = nn." + params.loss_func + "()\n";
  var linear_init = "";
  var metrics = "        self.metrics = [Metric_Accuracy()]\n\n";

  var loss_func =
    "     # y_: label\n     # y: model output from forward method\n     def loss(self, y, y_):\n          return self.lossFn(y, y_.view(-1))\n";
  var add_to_metric_func =
    "     # This method is optional, only used when metrics \n     # other than loss is desired\n     def add_to_metric(self, y, y_):\n          y_decoded = torch.argmax(y, dim=1)\n          self.metrics[0].append(y_decoded, y_.view(-1))\n";
  var forward_func = "    def forward(self, x):\n        out_1 = x\n";

  // construct graph
  let graph = new Map();
  graph = createGraph(state);

  // init functions
  linear_init += GenerateInitFunctions(graph);

  // construct forward function (bfs)
  var input_node = graph.get(1);
  var queue = [input_node];
  var visited = [];
  while (queue.length > 0) {
    var node = queue.shift();
    if (!visited.includes(node)) {
      visited.push(node);
      var tmp;
      if (node.type == "Linear") {
        tmp = forward_linear(node);
        if (tmp == "") {
          return {
            msg: "too many inputs for linear function, node id: " + node.id,
            code: "",
          };
        } else {
          forward_func += tmp;
        }
      } else if (node.type == "Conv") {
        tmp = forward_conv(node);
        if (tmp == "") {
          return {
            msg: "too many inputs for conv function, node id: " + node.id,
            code: "",
          };
        } else {
          forward_func += tmp;
        }
      } else if (node.type == "add") {
        tmp = forward_add(node);
        if (tmp == "") {
          return {
            msg: "missing input for add, node id: " + node.id,
            code: "",
          };
        } else {
          forward_func += tmp;
        }
      } else if (node.type == "concat") {
        forward_func += forward_concat(node);
      } else if (node.type == "MaxPool" || node.type == "AvgPool") {
        forward_func += forward_pool(node);
      } else if (node.type == "Flatten") {
        forward_func += forward_flatten(node);
      }

      for (var i in node.out_nodes) {
        queue.push(graph.get(node.out_nodes[i]));
      }
    }
  }
  forward_func = forward_func + "        return F.softmax(out_2,dim=1)\n";

  var outputcode =
    header +
    optAndRate +
    initialize_func +
    lossFn +
    linear_init +
    metrics +
    loss_func +
    add_to_metric_func +
    forward_func;

  return {
    msg: "Generated Code",
    code: outputcode,
  };
}
