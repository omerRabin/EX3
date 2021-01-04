from numpy.core import double
from Edge_Data import Edge_Data


class Node:

    def __init__(self, node_id: int, pos: tuple[double, double, double], info: str, tag: double,
                 edges: dict[int, Edge_Data]):
        self.pos = pos
        self.node_id = node_id
        self.info = info
        self.tag = tag
        self.edges = edges

    def getEdges(self):
        # return the dict-Edges of self Node
        return self.edges

    def getWeight(self, id2):
        # return the weight between self to node2
        return self.edges.get(id2).w
