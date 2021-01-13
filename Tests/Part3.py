import json
import time
import unittest

import matplotlib.pyplot as plt

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import networkx as nx

class MyTestCase(unittest.TestCase):#omer, u need to change that to C:/Users/omer rabin/PycharmProjects/Ex3/data/...
    graph1 = "C:/Users/digorker/PycharmProjects/Ex3/data/G_10_80_1.json"
    graph2 = "C:/Users/digorker/PycharmProjects/Ex3/data/G_100_800_1.json"
    graph3 = "C:/Users/digorker/PycharmProjects/Ex3/data/G_1000_8000_1.json"
    graph4 = "C:/Users/digorker/PycharmProjects/Ex3/data/G_10000_80000_1.json"
    graph5 = "C:/Users/digorker/PycharmProjects/Ex3/data/G_20000_160000_1.json"
    graph6 = "C:/Users/digorker/PycharmProjects/Ex3/data/G_30000_240000_1.json"
    graphs = [graph1, graph2, graph3, graph4, graph5, graph6]

    def buildGraph(size: int) -> DiGraph:
        g = DiGraph()
        for i in range(size):
            g.add_node(i)
        return g

    def printThePath(shortest: tuple) -> None:
        dist = shortest[0]
        path = shortest[1]
        if path is not None:
            print("Path between ", path[0], "to", path[len(path) - 1], ":")
            for i in range(len(path)):
                print(path[i], sep=",")
        else:
            print("There is no path between the two")

    def OurShortestPath(file_path: str, src: int, dest: int) -> float:
        algo = GraphAlgo(None)
        algo.load_from_json(file_path)
        # algo.plot_graph() #this may help understanding errors
        start_time = time.perf_counter()
        path = algo.shortest_path(src, dest)#cheking the time passed from start to finish
        end_time = time.perf_counter()
        myCodeTime = end_time - start_time
        # print_path(path)
        return myCodeTime

    def nx_shortest_path(file_path: str, src: int, dest: int) -> float:
        g = GraphAlgo(None)
        g.load_from_json(file_path)
        start_time_nx = time.perf_counter()
        nx.shortest_path(g, source=src, target=dest, weight='weight')
        end_time_nx = time.perf_counter()
        time_nx = end_time_nx - start_time_nx
        # print("time_nx in shortest path:", time_nx, "\n")
        return time_nx


if __name__ == '__main__':
    unittest.main()
