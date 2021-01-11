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
        ga.load_from_json("C:/Users/omer rabin/PycharmProjects/EX3/DATA/G_10_80_1.json");
        self.assertEqual(ga.save_to_json("save_test.json"), True)


if __name__ == '__main__':
    unittest.main()
