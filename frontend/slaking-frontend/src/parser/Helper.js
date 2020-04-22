export function GenerateInitFunctions(graph) {
  var linear_id = [];
  var in_size;
  var out_size;
  var linear_init = "";
  for (let [id, node] of graph.entries()) {
    console.log(id, node);
    if (node.type == "Linear") {
      linear_id.push(id);
      in_size = node.parameters.in;
      out_size = node.parameters.out;
      linear_init =
        linear_init +
        "        self.linear" +
        id +
        " = nn.Linear(" +
        in_size +
        ", " +
        out_size +
        ")\n";
    } else if (node.type == "Conv") {
      linear_id.push(id);
      in_size = node.parameters.in;
      out_size = node.parameters.out;
      linear_init =
        linear_init +
        "        self.conv" +
        id +
        " = nn.Conv" +
        node.parameters.dimension +
        "d(" +
        in_size +
        ", " +
        out_size +
        ", " +
        node.parameters.kernel_size +
        ", stride=" +
        node.parameters.stride +
        ", padding=" +
        node.parameters.padding +
        ", padding_mode='" +
        node.parameters.padding_mode +
        "'" +
        ")\n";
    } else if (node.type == "MaxPool" || node.type == "AvgPool") {
      linear_init =
        linear_init +
        "        self.pool" +
        id +
        " = nn." +
        node.type +
        node.parameters.dimension +
        "d(" +
        node.parameters.kernel_size +
        ", stride=" +
        node.parameters.stride +
        ", padding=" +
        node.parameters.padding +
        ")\n";
    } else if (node.type == "Flatten") {
      linear_init =
        linear_init +
        "        self.flatten" +
        id +
        " = nn." +
        node.type +
        "(start_dim=" +
        node.parameters.start_dim +
        ")\n";
    }
  }
  return linear_init;
}

export function forward_linear(node) {
  var forward_func = "";
  if (node.in_nodes.length > 1) {
    return "";
  } else {
    forward_func =
      forward_func +
      "        " +
      "out_" +
      
      node.id +
      " = self.linear" +
      node.id +
      "(out_" +
      node.in_nodes[0] +
      ")\n";
    forward_func =
      forward_func +
      "         " +
      "out_" +
      node.id +
      " = F.relu(" +
      "out_" +
      node.id +
      ")\n";
  }
  return forward_func;
}

export function forward_add(node) {
  var forward_func = "";
  if (node.in_nodes.length != 2) {
    return "";
  }
  forward_func =
    forward_func +
    "        " +
    "out_" +
    node.id +
    " = " +
    "out_" +
    node.in_nodes[0] +
    " + out_" +
    node.in_nodes[0] +
    "\n";
  return forward_func;
}

export function forward_concat(node) {
  var forward_func = "        " + "out_" + node.id + " = torch.cat(";
  for (var idx in node.in_nodes) {
    if (idx == 0) forward_func = forward_func + "out_" + node.in_nodes[idx];
    else forward_func = forward_func + ", out_" + node.in_nodes[idx];
  }
  forward_func = forward_func + ")\n";
  return forward_func;
}

export function forward_conv(node) {
  var forward_func = "";
  if (node.in_nodes.length > 1) {
    return "";
  } else {
    forward_func =
      forward_func +
      "        " +
      "out_" +
      node.id +
      " = self.conv" +
      node.id +
      "(out_" +
      node.in_nodes[0] +
      ")\n";
    forward_func =
      forward_func +
      "         " +
      "out_" +
      node.id +
      " = F.relu(" +
      "out_" +
      node.id +
      ")\n";
  }
  return forward_func;
}

export function forward_pool(node) {
  var forward_func = "";
  if (node.in_nodes.length > 1) {
    return "";
  } else {
    forward_func =
      forward_func +
      "        " +
      "out_" +
      node.id +
      " = self.pool" +
      node.id +
      "(out_" +
      node.in_nodes[0] +
      ")\n";
  }
  return forward_func;
}

export function forward_flatten(node) {
  var forward_func = "";
  if (node.in_nodes.length > 1) {
    return "";
  } else {
    forward_func =
      forward_func +
      "        " +
      "out_" +
      node.id +
      " = self.flatten" +
      node.id +
      "(out_" +
      node.in_nodes[0] +
      ")\n";
  }
  return forward_func;
}
