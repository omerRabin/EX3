import json
import time
import unittest

import matplotlib.pyplot as plt

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
import networkx as nx

#omer, u need to change that to C:/Users/omer rabin/PycharmProjects/Ex3/data/... and mine is "C:/Users/digorker/PycharmProjects/Ex3/data/
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

def our_connected_components(file_path: str) -> float:
    algo = GraphAlgo()
    algo.load_from_json(file_path)
    start_time = time.perf_counter()
    ccs = algo.connected_components()
    end_time = time.perf_counter()
    # print("all scc in g:", ccs, "\n")
    myCodeTime = end_time - start_time
    return myCodeTime

def nx_CCs(file_path: str) -> float:
    g = GraphAlgo(None)
    g.load_from_json(file_path)
    start_time_nx = time.perf_counter()
    ccs_nx = list(nx.strongly_connected_components(g))
    end_time_nx = time.perf_counter()
    time_nx = end_time_nx - start_time_nx
    # print("all scc in g:", ccs_nx, "\n")
    return time_nx

def our_CC(file_path: str, id1: int, ) -> float:
    algo = GraphAlgo(None)
    algo.load_from_json(file_path)
    start_time = time.perf_counter()
    cc = algo.connected_component(id1)
    end_time = time.perf_counter()
    # print("cc in g for specific node:", cc, "\n")
    return end_time - start_time

class MyTestCase(unittest.TestCase):
    def test__G_10_80_1(self):
        file_path = "C:/Users/digorker/PycharmProjects/Ex3/data/G_10_80_1.json"
        print("Graph 1:")
        oCCsTime = our_connected_components(file_path)
        oCCTime = our_CC(file_path, 1)
        oSPTime = OurShortestPath(file_path, 0, 5)
        nxCCsTime = nx_CCs(file_path)
        nxSPTime = nx_shortest_path(file_path, 0, 5)
        print("our time for SCCs:", oCCsTime)
        print("networkx time for SCCs:", nxCCsTime)
        print("our time for one SCC:", oCCTime)
        print("our time for shortest_path:", oSPTime)
        print("networkx time for shortest_path:", nxSPTime)

    def test__G_100_800_1(self):
        file_path = "C:/Users/digorker/PycharmProjects/Ex3/data/G_100_800_1.json"
        print("Graph 2:")
        oCCsTime = our_connected_components(file_path)
        oCCTime = our_CC(file_path, 1)
        oSPTime = OurShortestPath(file_path, 0, 5)
        nxCCsTime = nx_CCs(file_path)
        nxSPTime = nx_shortest_path(file_path, 0, 5)
        print("our time for SCCs:", oCCsTime)
        print("networkx time for SCCs:", nxCCsTime)
        print("our time for one SCC:", oCCTime)
        print("our time for shortest_path:", oSPTime)
        print("networkx time for shortest_path:", nxSPTime)

    def test__G_1000_8000_1(self):
        file_path = "C:/Users/digorker/PycharmProjects/Ex3/data/G_1000_8000_1.json"
        print("Graph 3:")
        oCCsTime = our_connected_components(file_path)
        oCCTime = our_CC(file_path, 1)
        oSPTime = OurShortestPath(file_path, 0, 5)
        nxCCsTime = nx_CCs(file_path)
        nxSPTime = nx_shortest_path(file_path, 0, 5)
        print("our time for SCCs:", oCCsTime)
        print("networkx time for SCCs:", nxCCsTime)
        print("our time for one SCC:", oCCTime)
        print("our time for shortest_path:", oSPTime)
        print("networkx time for shortest_path:", nxSPTime)

    def test__G_10000_80000_1(self):
        file_path = "C:/Users/digorker/PycharmProjects/Ex3/data/G_10000_80000_1.json"
        print("Graph 4:")
        oCCsTime = our_connected_components(file_path)
        oCCTime = our_CC(file_path, 1)
        oSPTime = OurShortestPath(file_path, 0, 5)
        nxCCsTime = nx_CCs(file_path)
        nxSPTime = nx_shortest_path(file_path, 0, 5)
        print("our time for SCCs:", oCCsTime)
        print("networkx time for SCCs:", nxCCsTime)
        print("our time for one SCC:", oCCTime)
        print("our time for shortest_path:", oSPTime)
        print("networkx time for shortest_path:", nxSPTime)

    def test__G_20000_160000_1(self):
        file_path = "C:/Users/digorker/PycharmProjects/Ex3/data/G_20000_160000_1.json"
        print("Graph 5:")
        oCCsTime = our_connected_components(file_path)
        oCCTime = our_CC(file_path, 1)
        oSPTime = OurShortestPath(file_path, 0, 5)
        nxCCsTime = nx_CCs(file_path)
        nxSPTime = nx_shortest_path(file_path, 0, 5)
        print("our time for SCCs:", oCCsTime)
        print("networkx time for SCCs:", nxCCsTime)
        print("our time for one SCC:", oCCTime)
        print("our time for shortest_path:", oSPTime)
        print("networkx time for shortest_path:", nxSPTime)

    def test__G_30000_240000_1(self):
        file_path = "C:/Users/digorker/PycharmProjects/Ex3/data/G_30000_240000_1.json"
        print("Graph 6:")
        oCCsTime = our_connected_components(file_path)
        oCCTime = our_CC(file_path, 1)
        oSPTime = OurShortestPath(file_path, 0, 5)
        nxCCsTime = nx_CCs(file_path)
        nxSPTime = nx_shortest_path(file_path, 0, 5)
        print("our time for SCCs:", oCCsTime)
        print("networkx time for SCCs:", nxCCsTime)
        print("our time for one SCC:", oCCTime)
        print("our time for shortest_path:", oSPTime)
        print("networkx time for shortest_path:", nxSPTime)


if __name__ == '__main__':
    unittest.main()
