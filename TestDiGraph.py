import unittest

from DiGraph import DiGraph


class TestDiGraph(unittest.TestCase):

    def setUp(self):
        self.g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        change_x = 0.000242
        change_y = 0.000328
        for n in range(4):
            self.g.add_node(n, (x, y))
        self.g.add_edge(0, 1, 1)
        self.g.add_edge(1, 0, 1.1)
        self.g.add_edge(1, 2, 1.3)
        self.g.add_edge(2, 3, 1.1)
        self.g.add_edge(1, 3, 1.9)
        self.g.remove_edge(1, 3)
        self.g.add_edge(1, 3, 10)

    def test_v_size(self):
        # normal check
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        change_x = 0.000242
        change_y = 0.000328
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_node(5, (3, 3))
        g.add_edge(1, 3, 2)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 4)
        self.assertEqual(g.v_size(), 5)

        # checking if a nod ewith the same id is added, will the size change or not
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        change_x = 0.000242
        change_y = 0.000328
        for n in range(10):
            g.add_node(n, (x, y))
        g.add_edge(1, 3, 2)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 4)
        g.add_node(2, (2, 4))
        self.assertEqual(g.v_size(), 10)

        # checking how will the size change if we remove a node
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        change_x = 0.000242
        change_y = 0.000328
        for n in range(10):
            g.add_node(n, (x, y))
        g.add_edge(1, 3, 2)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 4)
        g.remove_node(2)
        self.assertEqual(g.v_size(), 9)

    def test_e_size(self):
        # noraml check
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        change_x = 0.000242
        change_y = 0.000328
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(1, 2, 3)
        g.add_edge(1, 3, 3)
        z = 2
        self.assertEqual(g.e_size(), 2)

        # checking how will the size change if we the same edge is added
        # the size shouldn't change
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        change_x = 0.000242
        change_y = 0.000328
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(1, 3, 2)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 4)
        g.add_edge(1, 2, 4)
        self.assertEqual(g.e_size(), 3)

        # checking how will the size change if we remove an edge
        # the size shouldn't change
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        change_x = 0.000242
        change_y = 0.000328
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(1, 3, 2)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 4)
        g.remove_edge(1, 2)
        self.assertEqual(g.e_size(), 2)

    def test_get_all_v(self):
        # normal check
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        change_x = 0.000242
        change_y = 0.000328
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(1, 3, 2)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 4)
        nodes = g.get_all_v()
        p_list = []
        for n in nodes:
            p_list.append(nodes.get(n).getPos())
        list_tuple = [(x, y), (x, y), (x, y), (x, y)]
        self.assertEqual(list_tuple, p_list)

        # check if node is removed mid code
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        change_x = 0.000242
        change_y = 0.000328
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(1, 3, 2)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 4)
        g.remove_node(2)
        nodes = g.get_all_v()
        p_list = []
        for n in nodes:
            p_list.append(nodes.get(n).getPos())
        list_tuple = [(x, y), (x, y), (x, y)]
        self.assertEqual(list_tuple, p_list)

        # check if node is added mid code
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        change_x = 0.000242
        change_y = 0.000328
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(1, 3, 2)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 4)
        g.add_node(5, (2, 3))
        nodes = g.get_all_v()
        p_list = []
        for n in nodes:
            p_list.append(nodes.get(n).getPos())
        list_tuple = [(x, y), (x, y), (x, y), (x, y), (2, 3)]
        self.assertEqual(list_tuple, p_list)

    def test_all_in_edges_of_node(self):
        # normal check
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(1, 3, 2)
        g.add_edge(0, 1, 1)
        g.add_edge(2, 1, 1.2)
        g.add_edge(1, 2, 4)
        nodes = g.all_in_edges_of_node(1)
        nodes_keys = nodes.keys()
        nodes_v = nodes.values()
        nodes_v = list(nodes_v)

        self.assertEqual(nodes_keys, {0, 2})
        self.assertEqual(nodes_v, [1, 1.2])

        # check if edge is removed mid code
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(1, 3, 2)
        g.add_edge(0, 1, 1)
        g.add_edge(2, 1, 1.2)
        g.add_edge(1, 2, 4)
        g.remove_edge(2, 1)
        nodes = g.all_in_edges_of_node(1)
        nodes_keys = nodes.keys()
        nodes_v = nodes.values()
        nodes_v = list(nodes_v)
        self.assertEqual(nodes_keys, {0})
        self.assertEqual(nodes_v, [1])

        # check if edge is added mid code
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(1, 3, 2)
        g.add_edge(0, 1, 1)
        g.add_edge(2, 1, 1.2)
        g.add_edge(1, 2, 4)
        g.add_edge(3, 1, 0.24)
        nodes = g.all_in_edges_of_node(1)
        nodes_keys = nodes.keys()
        nodes_v = nodes.values()
        nodes_v = list(nodes_v)
        self.assertEqual(nodes_keys, {0, 2, 3})
        self.assertEqual(nodes_v, [1, 1.2, 0.24])

    def test_all_out_edges_of_node(self):
        # normal check
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(1, 3, 2)
        g.add_edge(0, 1, 1)
        g.add_edge(2, 1, 1.2)
        g.add_edge(1, 2, 4)
        nodes = g.all_out_edges_of_node(1)
        nodes_keys = nodes.keys()
        nodes_v = nodes.values()
        nodes_v = list(nodes_v)
        self.assertEqual(nodes_keys, {3, 2})
        self.assertEqual(nodes_v, [2, 4])

        # check what happens if we add a edge mid code
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(1, 3, 2)
        g.add_edge(0, 1, 1)
        g.add_edge(2, 1, 1.2)
        g.add_edge(1, 2, 4)
        g.add_edge(1, 0, 4)
        nodes = g.all_out_edges_of_node(1)
        nodes_keys = nodes.keys()
        nodes_v = nodes.values()
        nodes_v = list(nodes_v)
        self.assertEqual(nodes_keys, {3, 2, 0})
        self.assertEqual(nodes_v, [2, 4, 4])

        # check what happens if we add a edge mid code
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(1, 3, 2)
        g.add_edge(0, 1, 1)
        g.add_edge(2, 1, 1.2)
        g.add_edge(1, 2, 4)
        g.remove_edge(1, 3)
        nodes = g.all_out_edges_of_node(1)
        nodes_keys = nodes.keys()
        nodes_v = nodes.values()
        nodes_v = list(nodes_v)
        self.assertEqual(nodes_keys, {2})
        self.assertEqual(nodes_v, [4])

    def test_get_mc(self):
        # normal check
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(1, 3, 2)
        g.add_edge(0, 1, 1)
        g.add_edge(2, 1, 1.2)
        g.add_edge(1, 2, 4)
        self.assertEqual(g.get_mc(), 8)

        # check removal/change mid code
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(1, 3, 2)
        g.add_edge(0, 1, 1)
        g.add_edge(2, 1, 1.2)
        g.add_edge(1, 2, 4)
        self.assertEqual(g.get_mc(), 8)
        g.remove_edge(1, 2)
        g.remove_node(0)
        self.assertEqual(g.get_mc(), 10)

    def test_add_edge(self):
        # checking if the edge is added
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(1, 3, 2)

        Edges = g.get_all_edges()
        Edges = Edges[0]
        self.assertEqual(Edges.get_src(), 1)
        self.assertEqual(Edges.get_dest(), 3)
        self.assertEqual(Edges.get_weight(), 2)

        # checking that an edge with unexisting node src will not be added
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        # non existing node src 6
        g.add_edge(6, 3, 2)
        Edges = g.get_all_edges()
        self.assertEqual(Edges, [])

        # checking that an edge with unexisting node dest will not be added
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        # non existing node dest 7
        g.add_edge(2, 7, 2)
        Edges = g.get_all_edges()
        self.assertEqual(Edges, [])

    def test_add_node(self):
        # normacl check
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        nodes = g.get_all_v()
        nodes_keys = nodes.keys()
        nodes_keys = list(nodes_keys)
        list1 = [0, 1, 2, 3]
        self.assertEqual(list1, nodes_keys)
        nodes_values = nodes.values()
        p_list = []
        for n in nodes:
            p_list.append(nodes.get(n).getPos())
        list_tuple = [(x, y), (x, y), (x, y), (x, y)]
        self.assertEqual(list_tuple, p_list)

        # checking adding a node with existing id won't happen
        # we add a node with same id but different pos
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_node(1, (2, 3))
        nodes = g.get_all_v()
        nodes_keys = nodes.keys()
        nodes_keys = list(nodes_keys)
        list1 = [0, 1, 2, 3]
        self.assertEqual(list1, nodes_keys)
        nodes_values = nodes.values()
        p_list = []
        for n in nodes:
            p_list.append(nodes.get(n).getPos())
        list_tuple = [(x, y), (x, y), (x, y), (x, y)]
        self.assertEqual(list_tuple, p_list)

    def test_remove_node(self):
        # normal check
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(3, 1, 2)
        g.add_edge(1, 2, 1)
        g.add_edge(1, 0, 1.2)
        g.remove_node(1)
        nodes = g.get_all_v()
        node_id = []
        for n in nodes:
            node_id.append(nodes.get(n).getId())
        self.assertEqual(node_id, [0, 2, 3])

        # checking removing a non existing node
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(3, 1, 2)
        g.add_edge(1, 2, 1)
        g.add_edge(1, 0, 1.2)
        g.remove_node(1)
        g.remove_node(7)
        nodes = g.get_all_v()
        node_id = []
        for n in nodes:
            node_id.append(nodes.get(n).getId())
        self.assertEqual(node_id, [0, 2, 3])

    def test_remove_edge(self):
        #normal check
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(3, 1, 2)
        g.add_edge(1, 2, 1)
        g.add_edge(1, 0, 1.2)

        g.remove_edge(3, 1)
        edges = g.get_all_edges()
        self.assertEqual(len(edges), 2)
        edge = edges[0]
        self.assertEqual(edge.get_src(), 1)
        self.assertEqual(edge.get_dest(), 2)
        self.assertEqual(edge.get_weight(), 1)
        edge = edges[1]
        self.assertEqual(edge.get_src(), 1)
        self.assertEqual(edge.get_dest(), 0)
        self.assertEqual(edge.get_weight(), 1.2)

        # checking removing a non existing edge
        g = DiGraph()
        x = 35.19805902663438
        y = 32.10525428067227
        for n in range(4):
            g.add_node(n, (x, y))
        g.add_edge(3, 1, 2)
        g.add_edge(1, 2, 1)
        g.add_edge(1, 0, 1.2)

        g.remove_edge(3, 1)
        g.remove_edge(7, 1)
        edges = g.get_all_edges()
        self.assertEqual(len(edges), 2)
        edge = edges[0]
        self.assertEqual(edge.get_src(), 1)
        self.assertEqual(edge.get_dest(), 2)
        self.assertEqual(edge.get_weight(), 1)
        edge = edges[1]
        self.assertEqual(edge.get_src(), 1)
        self.assertEqual(edge.get_dest(), 0)
        self.assertEqual(edge.get_weight(), 1.2)


if __name__ == '__main__':
    unittest.main()
