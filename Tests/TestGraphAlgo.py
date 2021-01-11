import unittest
from GraphAlgo import GraphAlgo


def init():
    ga = GraphAlgo()
    return ga


class TestGraphAlgo(unittest.TestCase):

    def test_loadFromJson(self):
        ga = init()
        self.assertEqual(ga.load_from_json("C:/Users/omer rabin/PycharmProjects/EX3/DATA/G_10_80_1.json"), True)
        self.assertEqual(ga.load_from_json("blabla"), False)

    def test_SaveToJson(self):
        ga = init()
        ga.load_from_json("C:/Users/omer rabin/PycharmProjects/EX3/DATA/G_10_80_1.json")
        self.assertEqual(ga.save_to_json("save_test.json"), True)

    def test_shortest_path(self):
        g_algo = GraphAlgo()
        g_algo.graph.add_node(0)
        g_algo.graph.add_node(1)
        g_algo.graph.add_node(2)
        g_algo.graph.add_node(0, [1, 1, 0])
        g_algo.graph.add_node(1, [2, 4, 0])
        self.assertEqual(g_algo.shortest_path(0, 1), (1, [0, 1]))
        self.assertEqual(g_algo.shortest_path(0, 2), (5, [0, 1, 2]))

    def test_plot_graph(self):
        ga = init()
        ga.load_from_json("C:/Users/omer rabin/PycharmProjects/EX3/DATA/G_10_80_1.json")
        ga.plot_graph()


if __name__ == '__main__':
    unittest.main()
