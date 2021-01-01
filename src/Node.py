from typing import List
from Edge_Data import Edge_Data


class Node:

    def __init__(self, node_id: int, pos: tuple, ni: List[Node], info: str, tag: double, edge: Edge_Data):
        self.pos = pos
        self.node_id = node_id
        self.ni = ni
        self.info = info
        self.tag = tag
        self.edge = edge
