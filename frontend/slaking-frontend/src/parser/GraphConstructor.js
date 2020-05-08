/*
* @Author: Webster Bei Yijie, Joey Junyu Liang
* @Date: 5/8/2020, 3:24:14 PM
* @Email: yijie.bei@duke.edu, junyu.liang@duke.edu
*/


export function createGraph(state){
    if (! state.nodes.length>0 ) return "";
 
    var nodes = state.nodes;
    var links = state.links;
    
    let graphMap = new Map()
    // node.parameters: {
    //     in: 0,
    //     out: 0
    //   },

    var idx;
    var node;
    var link;
    for (idx in nodes){
        node = nodes[idx];
        graphMap.set(
            node.id,
            {
            id:node.id,
            type:node.type,
            parameters:node.parameters,
            in_nodes: [],
            out_nodes:[]
            }
        );
    }

    for (idx in links){
        link = links[idx];
        graphMap.get(link.from).out_nodes.push(link.to);
        graphMap.get(link.to).in_nodes.push(link.from);
    } 
        
    return graphMap;
}