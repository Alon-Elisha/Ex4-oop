import unittest
from threading import Thread

from GraphAlgo import GraphAlgo
from DiGraph import DiGraph
import time
import data

class TestGraphAlgo(unittest.TestCase):

    # in this code we only use this algorthms/function of the class
    # so we will expend only on that
    def test_shortest_path(self):
        # check 1
        g = GraphAlgo()
        g1 = g.get_graph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g1.add_node(n, (x, y))
        g1.add_edge(0, 1, 1)
        g1.add_edge(1, 0, 1.1)
        g1.add_edge(1, 2, 1.3)
        g1.add_edge(2, 3, 1.1)
        g1.add_edge(1, 3, 1.9)
        z = g.shortest_path(1, 2)
        self.assertEqual(z[0], 1.3)
        self.assertEqual(z[1], [1, 2])

        # check 2
        g = GraphAlgo()
        g1 = g.get_graph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(6):
            g1.add_node(n, (x, y))
        g1.add_edge(0, 1, 1)
        g1.add_edge(1, 0, 1.1)
        g1.add_edge(1, 2, 1.3)
        g1.add_edge(2, 3, 1.1)
        g1.add_edge(1, 3, 1.9)

        g1.add_edge(1, 4, 2.21)
        g1.add_edge(4, 3, 2)
        g1.add_edge(3, 5, 1.9)

        g1.add_edge(2, 5, 10)
        g1.add_edge(1, 5, 7.5)
        z = g.shortest_path(0, 5)
        self.assertEqual(z[0], 4.8)
        self.assertEqual(z[1], [0, 1, 3, 5])

        # check 3
        # check if given two nodes that don't have a path return -1 and empty list
        g = GraphAlgo()
        g.load_from_json('data/A1.json')
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(10):
            g1.add_node(n, (x, y))
        g1.add_edge(0, 1, 1)
        g1.add_edge(1, 0, 1.1)
        g1.add_edge(1, 2, 1.3)
        g1.add_edge(2, 3, 1.1)
        g1.add_edge(1, 3, 1.9)
        z = g.shortest_path(1, 7)
        self.assertEqual(z[0], -1)
        self.assertEqual(z[1], [])




    def test_tsp(self):
        g = GraphAlgo()
        g1 = g.get_graph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g1.add_node(n, (x, y))
        g1.add_edge(0, 1, 1)
        g1.add_edge(1, 0, 1.1)
        g1.add_edge(1, 2, 1.3)
        g1.add_edge(2, 3, 1.1)
        g1.add_edge(1, 3, 1.9)
        z = g.TSP([0, 1, 2])
        time.sleep(0.5)
        self.assertEqual(z[0], [0, 1, 2])
        time.sleep(0.5)
        self.assertEqual(z[1], 2.3)

    def test_center_point(self):
        g = GraphAlgo()
        g1 = g.get_graph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g1.add_node(n, (x, y))
        g1.add_edge(0, 1, 1)
        g1.add_edge(1, 0, 1.1)
        g1.add_edge(1, 2, 1.3)
        g1.add_edge(2, 3, 1.1)
        g1.add_edge(1, 3, 1.9)
        z = g.centerPoint()
        self.assertEqual(z[0],1)
        self.assertEqual(z[1], 1.9)






if __name__ == '__main__':
    unittest.main()