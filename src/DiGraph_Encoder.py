import json
from DiGraph import DiGraph
from Node import Node


# class for encode graph to json File
class DiGraph_Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, DiGraph):  # if is Graph Object
            node = NodeEncoder()  # call to NodeEncoder
            listEdges = []  # list for storage edges
            for i in obj.get_all_v():  # loop on the nodes in the graph
                edgeInList = obj.all_in_edges_of_node(i)
                for j in edgeInList:  # loop on the edges(in) list of the current node
                    edgeW = edgeInList.get(j)
                    listEdges.append({"src": j, "dest": i, "w": edgeW})
            return {
                'Nodes': [node.default(j) for j in list(obj.get_all_v().values())],  # insert the nodes to the json
                # using NodeEncoder class
                'Edges': [j for j in listEdges]  # insert the list of the edges to the json
            }
        return json.JSONEncoder.default(self, obj)


class NodeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Node):  # check if obj is Node Object
            if obj.getPos() is not None:  # The case we have a position to the node
                return {
                    'pos': str(obj.getPos()),
                    'id': obj.getNode_id()
                }
            else:   # The case we don't have a position to the node
                return {
                    'id': obj.getNode_id()
                }
        return json.JSONEncoder.default(self, obj)
