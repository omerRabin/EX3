import unittest

from DiGraph import DiGraph


def init():
    g = DiGraph()
    for i in range(10):
        g.add_node(i)
    return g


class TestDiGraph(unittest.TestCase):

    def test_mc(self):
        g = init()
        self.assertEqual(g.mc, 10)
        g.add_edge(1, 0, 2)
        self.assertEqual(g.mc, 11)
        g.remove_edge(1, 0)
        self.assertEqual(g.mc, 12)
        g.add_edge(0, 1, 3)
        g.add_edge(2, 1, 5)
        g.remove_node(1)
        self.assertEqual(g.mc, 17)
        g.add_edge(0, 1, 3)
        g.add_edge(0, 1, 3)
        g.remove_edge(g.mc, 19)

    def test_e_size(self):
        g = init()
        self.assertEqual(g.sizeEdges, 0)
        g.add_edge(0, 1, 3.2)
        self.assertEqual(g.sizeEdges, 1)
        g.remove_edge(0, 1)
        self.assertEqual(g.sizeEdges, 0)
        g.add_edge(0, 1, 7)
        g.add_edge(3, 1, 4.9)
        g.remove_node(1)
        self.assertEqual(g.sizeEdges, 0)

    def test_get_all_v(self):
        g = init()
        for i in g.graph.keys():
            self.assertEqual(True, i in g.graph.keys())

    def test_all_in_edges_of_node(self):
        g = init()
        g.add_edge(1, 0, 3)
        g.add_edge(0, 1, 6)
        g.add_edge(2, 1, 5.8)
        g.add_edge(1, 3, 3.1)
        g.add_edge(4, 1, 0.4)
        d = {0: 6, 2: 5.8, 4: 0.4}
        self.assertEqual(d, g.all_in_edges_of_node(1))
        g.remove_edge(0, 1)
        g.remove_edge(2, 1)
        g.remove_edge(4, 1)
        self.assertEqual({}, g.all_in_edges_of_node(1))

    def test_all_out_edges_of_node(self):
        g = init()
        g.add_edge(1, 0, 3)
        g.add_edge(0, 1, 6)
        g.add_edge(2, 1, 5.8)
        g.add_edge(1, 3, 3.1)
        g.add_edge(4, 1, 0.4)
        d = {0: 3, 3: 3.1}
        self.assertEqual(d, g.all_out_edges_of_node(1))
        g.remove_edge(1, 0)
        g.remove_edge(1, 3)
        self.assertEqual({}, g.all_out_edges_of_node(1))

    def test_v_size(self):
        g = init()
        self.assertEqual(g.sizeNodes, 10)
        g.add_edge(1, 0, 2)
        self.assertEqual(g.sizeNodes, 10)
        g.remove_edge(1, 0)
        self.assertEqual(g.sizeNodes, 10)
        g.add_edge(0, 1, 3)
        g.add_edge(2, 1, 5)
        g.remove_node(1)
        self.assertEqual(g.sizeNodes, 9)

    def test_addEdge(self):
        g = init()
        self.assertEqual(g.add_edge(0, 0, 2), False)
        self.assertEqual(g.add_edge(0, 10000, 3), False)
        self.assertEqual(g.add_edge(3, 4, 0), False)
        g.add_edge(3, 4, 5)
        self.assertEqual(4 in g.Ni.get(3).keys(), True)
        self.assertEqual(5 in g.Ni.get(3).keys(), False)
        self.assertEqual(4 in g.get_node(3).edges.keys(), True)
        self.assertEqual(6 in g.get_node(3).edges.keys(), False)
        g.add_edge(8, 9, 6.9)
        self.assertEqual(None, g.getNi(9).get(8), None)
        self.assertEqual(None, g.get_node(9).edges.get(8), None)

    def test_get_node(self):
        g = init()
        n = g.get_node(8)
        self.assertEqual(8, n.node_id)
        self.assertEqual(None, g.get_node(2333))
        g.remove_node(8)
        self.assertEqual(None, g.get_node(8))

    def test_add_node(self):
        g = init()
        self.assertEqual(2 in g.graph.keys(), True)
        self.assertEqual(999 in g.graph.keys(), False)

    def test_remove_node(self):
        g = init()
        self.assertEqual(False, g.remove_node(333))
        self.assertEqual(True, g.remove_node(3))
        self.assertEqual(g.get_node(3), None)
        g.add_edge(0, 1, 3334)
        g.add_edge(2, 1, 342)
        g.remove_node(1)
        self.assertEqual(g.get_node(0).edges.get(1), None)
        self.assertEqual(g.get_node(2).edges.get(1), None)
        self.assertEqual(g.Ni.get(0).get(1), None)
        self.assertEqual(g.Ni.get(2).get(1), None)

    def test_remove_edge(self):
        g = init()
        self.assertEqual(g.remove_edge(2, 3), False)
        self.assertEqual(g.remove_edge(2, 2), False)
        g.add_edge(6, 4, 8)
        self.assertEqual(g.remove_edge(6, 4), True)
        self.assertEqual(g.getNi(6).get(4), None)
        self.assertEqual(g.get_node(6).edges.get(4), None)


if __name__ == '__main__':
    unittest.main()
