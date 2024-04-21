import unittest
from src.jackw.main.structures.DirectedGraph import Graph, print_graph


class TreeTest(unittest.TestCase):
    def test_graph_initialise(self):
        test_graph = Graph()
        self.assertEqual({}.keys(), test_graph.get_vertices())
        self.assertEqual(0, test_graph.get_vertices_count())

    def test_graph_add_vertices(self):
        test_graph = Graph()
        test_graph.add_vertex("A")
        test_graph.add_vertex("E")
        test_graph.add_vertex("I")
        test_graph.add_vertex("O")
        test_graph.add_vertex("U")
        self.assertEqual({'A', 'E', 'I', 'O', 'U'}, test_graph.get_vertices())
        self.assertEqual(5, test_graph.get_vertices_count())

    def test_graph_add_edge(self):
        test_graph = Graph()
        test_graph.add_vertex("A")
        test_graph.add_vertex("E")
        test_graph.add_vertex("I")
        test_graph.add_vertex("O")
        test_graph.add_vertex("U")
        test_graph.add_edge("A", "E", 10)
        test_graph.add_edge("A", "I", 7)
        test_graph.add_edge("E", "I", 5)
        test_graph.add_edge("E", "O", 2)
        test_graph.add_edge("I", "O", 4)
        test_graph.add_edge("O", "U", 3)
        self.assertEqual({'A', 'E', 'I', 'O', 'U'}, test_graph.get_vertices())
        self.assertEqual(5, test_graph.get_vertices_count())

    def test_print_graph(self):
        test_graph = Graph()
        test_graph.add_vertex("A")
        test_graph.add_vertex("E")
        test_graph.add_vertex("I")
        test_graph.add_vertex("O")
        test_graph.add_vertex("U")
        test_graph.add_edge("A", "E", 10)
        test_graph.add_edge("A", "I", 7)
        test_graph.add_edge("E", "I", 5)
        test_graph.add_edge("E", "O", 2)
        test_graph.add_edge("I", "O", 4)
        test_graph.add_edge("O", "U", 3)
        self.assertEqual("A -> E Cost: 10\nA -> I Cost: 7\nE -> I Cost: 5\nE -> O Cost: 2\nI -> O Cost: 4\nO -> U Cost: 3\n", print_graph(test_graph))


if __name__ == '__main__':
    unittest.main()
