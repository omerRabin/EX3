from GraphInterface import GraphInterface
from Node import Node
from Edge_Data import Edge_Data


class DiGraph(GraphInterface):
    # class represent a directed weighted Graph
    def __init__(self, graph: dict[int, Node] = None, mc: int = 0, sizeNodes: int = 0, sizeEdges: int = 0,
                 Ni: dict[int, dict[int, Node]] = None):
        if Ni is None:
            Ni = {}
        if graph is None:
            graph = {}
        self.Ni = Ni  # neighbors dictionary of each node in the Graph
        self.graph = graph  # graph dictionary
        self.mc = mc  # count changes on Graph
        self.sizeNodes = sizeNodes  # number of nodes in the Graph
        self.sizeEdges = sizeEdges  # number of edges in the Graph

    def v_size(self):
        return self.sizeNodes

    def getNi(self, id1: int):
        return self.Ni.get(id1)

    def e_size(self):
        return self.sizeEdges

    def get_all_v(self):
        return self.graph

    def all_in_edges_of_node(self, id1: int):
        dictIn = {}  # an empty dictionary of all in edges
        it = iter(self.graph.values())  # define iterator on the Graph
        for i in self.graph:
            current = next(it)
            if self.getNi(current.node_id) is None:
                continue
            if self.getNi(current.node_id).get(id1) is not None:  # check if the node with the key in the parameter is
                # neighbor of the current node in the loop
                item = {current.node_id: current.getWeight(id1)}
                dictIn.update(item)  # adding the pair of key and weight to dictIn
        return dictIn

    def all_out_edges_of_node(self, id1: int):
        dictOut = {}  # an empty dictionary of all out edges
        n = self.get_node(id1)  # get the node object
        edges = n.getEdges().values()  # get all values of Edges dict
        it = iter(edges)
        for i in edges:
            current = next(it)
            item = {current.des: current.w}  # create a pair of key and weight
            dictOut.update(item)
        return dictOut

    def get_mc(self):
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float):
        if weight <= 0:  # if the weight is negative doesnt add
            return False
        if id1 == id2:
            return False
        n2 = self.get_node(id2)
        n1 = self.get_node(id1)
        e = Edge_Data(id1, id2, weight, "", 0)  # create the new edge as object
        if n1 is None or n2 is None:  # if n2 or n1 is None do nothing
            return False
        if self.getNi(id1) is not None:
            if id2 in self.getNi(id1).keys():  # if node 2 is already neighbor of node1
                return False
        item = {n2.node_id: e}
        n1.edges.update(item)
        item2 = {n2.node_id: n2}
        self.Ni.get(id1).update(item2)
        self.mc += 1
        self.sizeEdges += 1
        return True

    def get_node(self, node_id: int):
        #  this method return the node with the key in the parameter
        if node_id in self.graph:
            return self.graph.get(node_id)
        return None

    def add_node(self, node_id: int, pos: tuple = None):
        n = Node(node_id, pos, "", 0, {})
        if node_id not in self.graph:  # add only if n is not exist in the graph
            self.graph.update({node_id: n})
            self.Ni.update({node_id: {}})
            self.mc += 1
            self.sizeNodes += 1
            return True
        return False

    def remove_node(self, node_id: int):
        if node_id not in self.graph:  # if the node is not exist doesnt remove
            return False
        it = iter(self.graph.values())
        for i in self.graph:
            current = next(it)
            if self.getNi(current.node_id).get(node_id) is not None:  # check if the removal node is neighbor of current
                self.getNi(current.node_id).pop(node_id)  # remove the removal node from the neighbor dict of current
                current.edges.pop(node_id)  # remove the removal node from the edges dict of current
                self.sizeEdges += -1
        self.sizeNodes -= 1
        self.mc += 1
        self.graph.pop(node_id)  # remove the removal node from the Graph
        return True

    def remove_edge(self, node_id1: int, node_id2: int):
        n1 = self.get_node(node_id1)
        n2 = self.get_node(node_id2)
        if n1 is None or n2 is None:
            return False
        if self.getNi(node_id1) is None:
            return False
        if self.getNi(node_id1).get(node_id2) is None:  # if n2 is not neighbor of n1  do nothing
            return False
        self.getNi(node_id1).pop(node_id2)  # remove n2 from neighbors dict of n1
        n1.edges.pop(node_id2)  # remove the edge from neighbors dict of n1
        self.mc += 1
        self.sizeEdges += -1
        return True

    # equal between graphs
    def __eq__(self, other):
        return self.sizeNodes == other.sizeNodes and self.sizeEdges == other.sizeEdges
