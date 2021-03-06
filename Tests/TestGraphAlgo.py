import unittest

from GraphAlgo import GraphAlgo


def init():
    ga = GraphAlgo()
    return ga


class TestGraphAlgo(unittest.TestCase):

    def test_loadFromJson(self):
        ga = init()
        self.assertEqual(ga.load_from_json("C:/Users/omer rabin/PycharmProjects/EX3/data/G_10_80_1.json"), True)
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
        ga2.load_from_json('../data/T0.json_saved')
        self.assertEqual(ga1.graph, ga2.graph)  # check if the graphs is equals according to equals method

    def test_SaveToJson(self):
        ga = init()
        ga.load_from_json("C:/Users/omer rabin/PycharmProjects/EX3/data/G_10_80_1.json")
        self.assertEqual(ga.save_to_json("save_test.json"), True)

    def test_shortest_path(self):
        g_algo = GraphAlgo()
        g_algo.graph.add_node(0)
        g_algo.graph.add_node(1)
        g_algo.graph.add_node(2)
        g_algo.graph.add_node(3)
        g_algo.graph.add_edge(0, 1, 1)
        g_algo.graph.add_edge(1, 2, 4)
        self.assertEqual(g_algo.shortest_path(0, 1), (1, [0, 1]))
        self.assertEqual(g_algo.shortest_path(0, 2), (5, [0, 1, 2]))
        g_algo.graph.add_edge(0, 3, 8)
        g_algo.graph.add_edge(2, 3, 2.5)
        self.assertEqual(g_algo.shortest_path(0, 3), (7.5, [0, 1, 2, 3]))
        g_algo.graph.add_edge(3, 1, 2.8)
        self.assertEqual(g_algo.shortest_path(0, 1), (1, [0, 1]))

    def test_dfs(self):
        ga = init()
        for i in range(6):
            ga.graph.add_node(i)
        ga.graph.add_edge(1, 2, 4.2)
        ga.graph.add_edge(2, 4, 5.2)
        ga.graph.add_edge(2, 3, 0.9)
        ga.graph.add_edge(3, 5, 9)
        ga.graph.add_edge(4, 1, 0.8)
        l = ga.dfs_help(2, ga.graph)
        result = ga.graph.get_node(1) in l and ga.graph.get_node(2) in l and ga.graph.get_node(3) in l \
                 and ga.graph.get_node(4) in l and ga.graph.get_node(5) in l
        self.assertEqual(result, True)
        ga.graph.remove_edge(1, 2)
        l1 = ga.dfs_help(2, ga.graph)
        result1 = ga.graph.get_node(1) in l1 and ga.graph.get_node(2) in l1 and ga.graph.get_node(3) in l1 \
                 and ga.graph.get_node(4) in l1 and ga.graph.get_node(5) in l1
        self.assertEqual(result1, True)
        ga.graph.remove_edge(2, 3)
        l2 = ga.dfs_help(2, ga.graph)
        result2 = ga.graph.get_node(1) in l2 and ga.graph.get_node(2) in l2 and ga.graph.get_node(4) in l2
        self.assertEqual(result2, True)

    def test_connected_component(self):
        ga = init()
        for i in range(6):
            ga.graph.add_node(i)
        ga.graph.add_edge(1, 2, 4.2)
        ga.graph.add_edge(2, 4, 5.2)
        ga.graph.add_edge(2, 3, 0.9)
        ga.graph.add_edge(3, 5, 9)
        ga.graph.add_edge(4, 1, 0.8)
        l = ga.connected_component(2)
        result = ga.graph.get_node(1) in l and ga.graph.get_node(2) in l and ga.graph.get_node(4) in l
        self.assertEqual(result, True)
        ga1 = init()
        self.assertEqual([], ga1.connected_component(90))
        ga1.graph.add_node(0)
        self.assertEqual([ga.graph.get_node(0)], ga.connected_component(0))

    def test_connected_components(self):  # not work- fix and then do test
        ga = init()
        for i in range(6):
            ga.graph.add_node(i)
        ga.graph.add_edge(1, 2, 4.2)
        ga.graph.add_edge(2, 4, 5.2)
        ga.graph.add_edge(2, 3, 0.9)
        ga.graph.add_edge(3, 5, 9)
        ga.graph.add_edge(4, 1, 0.8)
        lists = ga.connected_components()
        result = [ga.graph.get_node(1), ga.graph.get_node(2), ga.graph.get_node(4)] in lists and \
                 [ga.graph.get_node(0)] in lists and [ga.graph.get_node(3)] in lists and [ga.graph.get_node(5)] in lists
        self.assertEqual(True, result)

    def test_plot_graph(self):
        ga = init()
        ga.load_from_json("C:/Users/omer rabin/PycharmProjects/EX3/data/A5")
        ga.plot_graph()


if __name__ == '__main__':
    unittest.main()
