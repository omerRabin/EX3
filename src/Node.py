from numpy.core import double
from Edge_Data import Edge_Data


class Node:

    def __init__(self, node_id: int, pos: tuple[double, double, double], ni: dict, info: str, tag: double,
                 edges: dict[int, Edge_Data]):
        self.pos = pos
        self.node_id = node_id
        self.ni = ni
        self.info = info
        self.tag = tag
        self.edges = edges

    def getNi(self):
        return self.ni

    def getEdges(self):
        return self.edges

    def getWeight(self, id2):
        return self.edges.get(id2).getWeight()
