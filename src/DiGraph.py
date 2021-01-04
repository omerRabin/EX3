from GraphInterface import GraphInterface
from Node import Node
from Edge_Data import Edge_Data


class DiGraph(GraphInterface):
    def __init__(self, graph: dict[int, Node], mc: int, sizeNodes: int, sizeEdges: int, Ni: dict[int,dict[int,Node]]):
        self.Ni = Ni
        self.graph = graph
        self.mc = mc
        self.sizeNodes = sizeNodes
        self.sizeEdges = sizeEdges

    def v_size(self):
        return self.sizeNodes

    def getNi(self, id1: int):
        return self.Ni.get(id1)

    def e_size(self):
        return self.sizeEdges

    def get_all_v(self):
        return self.graph

    def all_in_edges_of_node(self, id1: int):
        dictIn = {}
        it = iter(self.graph.values())
        for i in it:
            current = next(it)
            if self.getNi(current.node_id).get(id1) is not None:
                item = {current.node_id, current.getWeight(id1)}
                dictIn.update(item)
            return dictIn

    def all_out_edges_of_node(self, id1: int):
        dictOut = {}
        n = self.get_node(id1)
        edges = n.getEdges().values()
        it = iter(edges)
        for i in it:
            current = next(it)
            item={current.des,current.w}
            dictOut.update(item)
            return dictOut

    def get_mc(self):
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float):
        if weight <= 0:
            return False
        n2=self.get_node(id2)
        n1=self.get_node(id1)
        e=Edge_Data(id1, id2, weight, "", 0)
        if n2 is not None and n1 is not None:
            if self.getNi(id1).get(id2) is None:
                item={n2.node_id:e}
                n1.edges.update(item)
                self.getNi(id1).update({n2.node_id:n2})
                self.mc += 1
                self.sizeEdges += 1
                return True
        return False

    def get_node(self, node_id: int):
        if node_id in self.graph:
            return self.graph.get(node_id)
        return None

    def add_node(self, node_id: int, pos: tuple = None):
        n = Node(node_id, pos, "", 0, {})
        if node_id not in self.graph:
            self.graph.update({node_id: n})
            self.mc += 1
            self.sizeNodes += 1
            return True
        return False

    def remove_node(self, node_id: int):
        if node_id not in self.graph:
            return False
        it = iter(self.graph.values())
        for i in it:
            current=next(it)
            if self.getNi(current.node_id).get(node_id) is not None:
                self.getNi(current.node_id).pop(node_id)
                current.edges.pop(node_id)
                self.sizeEdges += -1
        self.sizeNodes += -1
        self.mc += 1
        self.graph.pop(node_id)
        return True

    def remove_edge(self, node_id1: int, node_id2: int):
        n1 = self.get_node(node_id1)
        n2 = self.get_node(node_id2)
        if n1 is None or n2 is None:
            return False
        if self.getNi(node_id1).get(node_id2) is None:
            return False
        self.getNi(node_id1).pop(node_id2)
        n1.edges.pop(node_id2)
        self.mc += 1
        self.sizeEdges += -1
        return True
