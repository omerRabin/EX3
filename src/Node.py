from numpy.core import double
from Edge_Data import Edge_Data


class Node:

    def __init__(self, node_id: int, pos: tuple, ni: dict, info: str, tag: double, edges: dict[Edge_Data]):
        self.pos = pos
        self.node_id = node_id
        self.ni = ni
        self.info = info
        self.tag = tag
        self.edges = edges

    def getNi(self):
        return self.ni

