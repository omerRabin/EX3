from GraphInterface import GraphInterface
from Node import Node
class DiGraph:
    def __init__(self, graph: dict[int, Node], mc: int, sizeNodes: int, sizeEdges: int):
        self.graph=graph
        self.mc=mc
        self.sizeNodes=sizeNodes
        self.sizeEdges=sizeEdges


    def v_size(self):
        return self.sizeNodes

    def e_size(self):
        return self.sizeEdges

    def get_all_v(self):
        return self.graph

    def all_in_edges_of_node(self, id1: int):
        dictIn={}
        it=iter(self.graph.values())
        for i in it:
            current=next(it)
            if current.getNi().get(id1) is not None:
                item={current.node_id,current.getWeight(id1)}
                dictIn.update(item)
            return dictIn

    def all_out_edges_of_node(self, id1: int):
        dictOut = {}
        n=self.get_node(id1)
        edges=n.getEdges().values()
        it = iter(edges)
        for i in it:
            current = next(it)
            item={current.des,current.w}
            dictOut.update(item)
            return dictOut

    def get_mc(self):
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float):

    def get_node(self, node_id: int):
        if node_id in self.graph:
            return self.graph.get(node_id)
            pass

    def add_node(self, node_id: int, pos: tuple = None):

    def remove_node(self, node_id: int):

    def remove_edge(self, node_id1: int, node_id2: int):