from src import GraphInterface
from src import Node
class DiGraph:
    def __init__(self, graph: dict[Node], mc: int, sizeNodes: int, sizeEdges: int):
        self.graph=graph
        self.mc=mc
        self.size=size
        self.sizeNodes=sizeNodes
        self.sizeEdges=sizeEdges


    def v_size(self):

    def e_size(self):

    def get_all_v(self):

    def all_in_edges_of_node(self, id1: int):

    def all_out_edges_of_node(self, id1: int):

    def get_mc(self):

    def add_edge(self, id1: int, id2: int, weight: float):

    def add_node(self, node_id: int, pos: tuple = None):

    def remove_node(self, node_id: int):

    def remove_edge(self, node_id1: int, node_id2: int):