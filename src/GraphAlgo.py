import json
import math
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

    def get_graph(self) -> DiGraph:
        return self.graph

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

    def dfs_help(self, id1: int, g: DiGraph) -> list:
        """
        this method get an id of node and return the SCC of this node in the graph use dfs algorithm
        """
        srcNode = g.get_node(id1)
        visited = [srcNode]
        stack = [srcNode]  # temp list of nodes
        while stack:
            node = stack[-1]  # the last node in the stack
            if node not in visited:
                visited.append(node)
            remove_from_stack = True
            if g.getNi(node.node_id) is not None:
                for n in g.getNi(node.node_id).keys():
                    n_in = g.get_node(n)
                    if n_in not in visited:
                        stack.append(n_in)
                        remove_from_stack = False
                        break
            if remove_from_stack:
                stack.pop()
        return visited

    def invert_graph(self) -> DiGraph:
        """
        this method reverse the edges in the graph and return a reverse graph
        """
        g_reverse = DiGraph()
        for i in self.graph.graph:  # loop for adding the nodes
            g_reverse.add_node(i)
        for j in self.graph.graph:  # loop for adding the edges
            edges = self.graph.all_out_edges_of_node(j)
            for k in edges:
                g_reverse.add_edge(k, j, edges.get(k))  # k is the des of the current edge and j is the src
        return g_reverse

    def init_nodes(self):
        """
        this method initialize the node fields that are needed to algo methods: tag and info
        """
        g = self.graph.graph
        for i in g:
            g.get(i).tag = math.inf  # initialize tag to infinity for shortest path
            g.get(i).info = ""  # initialize to "" for dfs

    def connected_component(self, id1: int):
        """""
        this method return the strongly connected component(SCC) that node id1 is a part of using tarjan algorithm
        we got help from: https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/
        """""
        path = []  # the list contains the SCC of the node
        if self.graph is None or id1 not in self.graph.get_all_v().keys():  # the case the graph is none or the node not
            # exist in the graph
            return path
        p_regular = self.dfs_help(id1, self.graph)
        g_rev = self.invert_graph()
        p_reverse = self.dfs_help(id1, g_rev)
        p_regular_keys = []  # for check contains
        p_reverse_keys = []  # for check contains
        # loops for insert the keys
        for w in p_regular:
            p_regular_keys.append(w.node_id)
        for z in p_reverse:
            p_reverse_keys.append(z.node_id)
            # check which list is bigger
        if len(p_regular) >= len(p_reverse):
            for _ in p_regular_keys:
                isIn = p_regular_keys[-len(p_regular_keys)] in p_reverse_keys  # check if the other list contain the key
                if isIn:
                    path.append(self.graph.get_node(p_regular_keys[-len(p_regular_keys)]))  # if contains, add the node
                p_regular_keys.pop(-len(p_regular_keys))  # remove for continue loop
        else:  # the other case- the other list is bigger
            for _ in p_reverse_keys:
                isIn = p_reverse_keys[-len(p_reverse_keys)] in p_regular_keys
                if isIn:
                    path.append(self.graph.get_node(p_reverse_keys[-len(p_reverse_keys)]))
                p_reverse_keys.pop(-len(p_reverse_keys))

        return path

    def connected_components(self):


    """
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

    def updatePositions(self):
        g = self.get_graph().graph
        for i in g:
            if g.get(i).pos is None:
                g.get(i).pos = (random.uniform(-1, 1), random.uniform(-1, 1), 0)

    def plot_graph(self):
        self.updatePositions()
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
