import json
from GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph




class GraphAlgo(GraphAlgoInterface):

    def get_graph(self):
        return self.graph

    def load_from_json(self, file_name: str):
        try:
            with open(file_name, 'r') as f:
                s = json.load(f)
            g = DiGraph()
            for node in s["Nodes"]:
                if "pos" in node:
                    pos = tuple(map(float, str(node["pos"]).split(",")))
                    g.add_node(node['id'], pos)
                else:
                    g.add_node(node['id'])

            for edge in s["Edges"]:
                g.add_edge(edge["src"], edge["dest"], edge["w"])
            self.graph = g
            return True
        except Exception as e:
            print(e)
            return False



    def save_to_json(self, file_name: str):
        """
        try:
            with open(file_name, 'w') as f:
                json.dump(self.graph, f, cls=DiGraphEncoder)#need to add
                return True
        except:
            return False
        """

    def shortest_path(self, id1: int, id2: int):
        path = []
        path = path + [id1]
        if id1 == id2:
            return path
        if not self.has_key(id1):
            return None
        for node in self[id1]:
            if node not in path:
                newpath = self.shortest_path(self, node, id2)
                if newpath: return newpath
        return None

    """
    def connected_component(self, id1: int):

    def connected_components(self):

    def plot_graph(self):
    """