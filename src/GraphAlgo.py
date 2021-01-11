import json
from typing import List

from DiGraph_Encoder import DiGraph_Encoder
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
import random
import matplotlib.pyplot as plt
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=DiGraph()):
        self.graph = graph

    def get_graph(self) -> dict:
        return self.graph.get_all_v()

    def load_from_json(self, file_name: str):
        try:
            with open(file_name, 'r') as f:
                s = json.load(f)
            g = DiGraph()
            for node in s["Nodes"]:  # convert json to Nodes
                if "pos" in node:
                    pos = tuple(map(float, str(node["pos"]).split(",")))
                    g.add_node(node['id'], pos)  # insert the nodes with pos
                else:
                    g.add_node(node['id'])  # insert the nodes without pos

            for edge in s["Edges"]:  # convert json to Edges
                g.add_edge(edge["src"], edge["dest"], edge["w"])
            self.graph = g
            return True

        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str):

        try:
            with open(file_name, 'w') as f:
                json.dump(self.graph, f, cls=DiGraph_Encoder)  # convert the graph to json by the class encoder
                return True

        except Exception as e:
            print(e)
            return False

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

    """""
     def shortest_path(self, id1: int, id2: int) -> (float, list):
         if id1 not in self.get_graph() or id2 not in self.get_graph():
             return (math.inf,[])
         if id1 is id2:
             return (0, [id1]) # bdika
         #init all varibales in node
         self.__init_all()
         q = PriorityQueue()
         node = self.graph.get_all_v()[id1]
         node.weight = 0
         q.put((node.weight, node))

         while not q.empty():
             v=q.get()[1]
             for edge in self.graph.all_out_edges_of_node(v.getId()).values():
                 u= self.graph.get_all_v()[edge.getDest()]
                 dist = edge.getW()+v.weight
                 if dist < u.weight:
                     u.weight=dist
                     u.info=v.getId()
                     q.put((u.weight,u))
         path = []
         dest = self.graph.get_all_v()[id2]
         if dest.weight is math.inf:
             return  (math.inf,[])
         path.append(dest.getId())
         str = dest.info
         while str != "":
             node = self.graph.get_all_v()[str]
             path.insert(0, node.getId())
             str = node.info
         return dest.weight,path
    """

    """
    def connected_component(self, id1: int):

    def connected_components(self):
    """
    """
    def connected_component(self, id1: int) -> list:

    def connected_components(self) -> List[list]:

    def plot_graph(self):
        all_nodes = self.graph.get_all_v()
        x = []
        y = []
        for i in all_nodes.values():
            if i.getPos():
                x.append(i.getPos()[0])
                y.append(i.getPos()[1])
            else:
                x_random = random.uniform(35.18, 35.2)
                y_random = random.uniform(32.1, 32.2)
                i.setPos((x_random, y_random, 0.0))
                x.append(x_random)
                y.append(y_random)
        n = [j for j in all_nodes.keys()]
        fig, ax = plt.subplots()
        ax.scatter(x, y)
        for p, txt in enumerate(n):
            ax.annotate(n[p], (x[p], y[p]))
        plt.plot(x, y, "black")
        for i in all_nodes.keys():
            for j in self.graph.all_out_edges_of_node(i):
                x1_coordinate = all_nodes.get(i).getPos()[0]
                y1_coordinate = all_nodes.get(i).getPos()[1]
                x2_coordinate = all_nodes.get(j).getPos()[0]
                y2_coordinate = all_nodes.get(j).getPos()[1]
                plt.arrow(x1_coordinate, y1_coordinate, (x2_coordinate - x1_coordinate),
                          (y2_coordinate - y1_coordinate), length_includes_head=True, width=0.000010,
                          head_width=0.00006, color='black')
        plt.title("Ex3")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()
    """
