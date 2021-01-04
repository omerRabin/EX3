import unittest

from DiGraph import DiGraph


def init():
    g = DiGraph()
    for i in range(10):
        g.add_node(i)
    return g


class TestDiGraph(unittest.TestCase):

    def test_v_size(self):
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


if __name__ == '__main__':
    unittest.main()
