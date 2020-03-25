import { createGraph } from "./GraphConstructor";

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

    var header = "import torch\nimport torch.nn as nn\nimport torch.nn.functional as F\nfrom metrics import *\n\nclass Model():\n"
    var optAndRate = "     optimizer = \""+ params.optimizer+ "\"\n     learning_rate = "+ params.learning_rate+ "\n\n"

    var initialize_func = "     # initialize method is called once before forward and loss methods are called\n     def initialize(self):\n"
    var lossFn = "        self.lossFn = nn." +params.loss_func+"()\n"
    var linear_init = ""
    var metrics = "        self.metrics = [Metric_Accuracy()]\n\n"


    var loss_func = "     # y_: label\n     # y: model output from forward method\n     def loss(self, y, y_):\n          return self.lossFn(y, y_.view(-1))\n"
    var add_to_metric_func = "     # This method is optional, only used when metrics other than loss is desired\n     def add_to_metric(self, y, y_):\n          y_decoded = torch.argmax(y, dim=1)\n          self.metrics[0].append(y_decoded, y_.view(-1))\n"
    var forward_func = "    def forward(self, x):\n        out_1 = x\n"

    // construct graph
    let graph = new Map();
    graph = createGraph(state);

    // iterate through map to record id for linearization
    var linear_id = [];
    var in_size;
    var out_size;
    for (let [id, node] of graph.entries()) {
        console.log(id, node)
        if (node.type == "linear") {
            linear_id.push(id);
            in_size = node.parameters.in;
            out_size = node.parameters.out;
            linear_init = linear_init+"        self.linear"+ id+ " = nn.Linear("+ in_size+ ", "+ out_size+ ")\n";
        }
    }

    // construct forward function (bfs)
    var input_node = graph.get("1");
    var queue = [input_node];
    while (queue.length > 0) {
        var node = queue.shift();
        if (node.type == "linear") {
            if (node.in_nodes.length > 1) {
                return {
                    msg: "multiple input for linear function, node id "+node.id,
                    code: ""
                }
            }
            else {
                forward_func= forward_func + "        "+ "out_"+ node.id+ " = self.linear"+ node.id+ "(out_"+ node.in_nodes[0]+ ")\n"
                forward_func= forward_func + "        "+ "out_"+ node.id+ " = F.relu("+ "out_"+ node.id+")\n"
            }
        } else if (node.type == "add"){
            if (node.in_nodes.length != 2) {
                return {
                    msg: "missing input for add, node id: "+node.id,
                    code: ""
                }
            }
            forward_func= forward_func + "        "+ "out_"+ node.id+" = "+"out_"+node.in_nodes[0]+ " + "+node.in_nodes[0]+"\n"
        } else if (node.type == "concat"){
            forward_func= forward_func + "        "+ "out_"+ node.id+" = torch.cat("
            for (var idx in node.in_nodes){
                if (idx==0) forward_func= forward_func + "out_"+ node.in_nodes[idx]
                else forward_func= forward_func + ", out_"+ node.in_nodes[idx]
            }
            forward_func= forward_func + ")\n"
        } 

        for (var i in node.out_nodes){
            queue.push(graph.get(node.out_nodes[i]))
        }
    }
    forward_func= forward_func + "        return F.softmax(out_2,dim=1)\n"


    var outputcode = header + optAndRate + initialize_func + lossFn + linear_init + metrics+ loss_func + add_to_metric_func + forward_func
    

    return {
        msg: "Generated Code",
        code: outputcode
    }

}