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
        ga1 = init()
        for i in range(4):
            ga1.graph.add_node(i)
        ga1.graph.add_edge(0, 1, 1)
        ga1.graph.add_edge(1, 0, 1.1)
        ga1.graph.add_edge(1, 2, 1.3)
        ga1.graph.add_edge(1, 3, 1.8)
        ga1.graph.add_edge(2, 3, 1)
        ga2 = GraphAlgo()
        ga2.load_from_json('../DATA/T0.json_saved')
        self.assertEqual(ga1.graph, ga2.graph)  # check if the graphs is equals according to equals method

    def test_SaveToJson(self):
        ga = init()
        ga.load_from_json("C:/Users/omer rabin/PycharmProjects/EX3/DATA/G_10_80_1.json")
        self.assertEqual(ga.save_to_json("save_test.json"), True)

    def test_shortest_path(self):  # a basic check- not enough complicated
        g_algo = GraphAlgo()
        g_algo.graph.add_node(0)
        g_algo.graph.add_node(1)
        g_algo.graph.add_node(2)
        g_algo.graph.add_edge(0, 1, 1)
        g_algo.graph.add_edge(1, 2, 4)
        self.assertEqual(g_algo.shortest_path(0, 1), (1, [0, 1]))
        self.assertEqual(g_algo.shortest_path(0, 2), (5, [0, 1, 2]))

    def test_plot_graph(self):
        ga = init()
        ga.load_from_json("C:/Users/omer rabin/PycharmProjects/EX3/DATA/G_10_80_1.json")
        ga.plot_graph()


if __name__ == '__main__':
    unittest.main()
