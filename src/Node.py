from Edge_Data import Edge_Data


class Node:

    def __init__(self, node_id: int, pos: tuple[float, float, float] = None, info: str = None, tag: float = 0,
                 edges: dict[int, Edge_Data] = None):
        if edges is None:
            edges = {}
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

    def getPos(self):
        return self.pos

    def getNode_id(self):
        return self.node_id
