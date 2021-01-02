from src import GraphAlgoInterface
#from networkx.readwrite import json_graph
class GraphAlgo:
def get_graph(self):

def load_from_json(self, file_name: str):
    with open(file_name) as file:
        js_graph = json.load(file)
    return json_graph.node_link_graph(js_graph)

def save_to_json(self, file_name: str):
    #networkx.write_gml(self.graph, str)
    #print json_graph.dumps()

def shortest_path(self, id1: int, id2: int):

def connected_component(self, id1: int):

def connected_components(self):

def plot_graph(self):