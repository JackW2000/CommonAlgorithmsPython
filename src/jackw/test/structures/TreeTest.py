import unittest
from src.jackw.main.structures import Tree


class TreeTest(unittest.TestCase):
    def test_tree_initialise(self):
        test_tree = Tree.Tree("A")
        self.assertEqual("A", test_tree.root.data)

    def test_tree_inorder_traversal_one_node(self):
        test_tree = Tree.Tree("A")
        inorder_traversal = test_tree.inorder_traversal(test_tree)
        self.assertEqual(['A'], inorder_traversal)

    def test_tree_print_root(self):
        test_tree = Tree.Tree("A")
        root_string = test_tree.print_root()
        self.assertEqual("Data: A Left node: None Right node: None", root_string)

    def test_tree_inorder_traversal_multiple_node(self):
        test_tree = Tree.Tree("A")
        test_tree.insert("D")
        test_tree.insert("P")
        test_tree.insert("A")
        test_tree.insert("B")
        test_tree.insert("R")
        inorder_traversal = test_tree.inorder_traversal(test_tree)
        self.assertEqual(['A', 'A', 'B', 'D', 'P', 'R'], inorder_traversal)

    def test_tree_preorder_traversal_multiple_node(self):
        test_tree = Tree.Tree("A")
        test_tree.insert("D")
        test_tree.insert("P")
        test_tree.insert("A")
        test_tree.insert("B")
        test_tree.insert("R")
        preorder_traversal = test_tree.preorder_traversal(test_tree)
        self.assertEqual(['A', 'A', 'D', 'B', 'P', 'R'], preorder_traversal)

    def test_tree_postorder_traversal_multiple_node(self):
        test_tree = Tree.Tree("A")
        test_tree.insert("D")
        test_tree.insert("P")
        test_tree.insert("A")
        test_tree.insert("B")
        test_tree.insert("R")
        postorder_traversal = test_tree.postorder_traversal(test_tree)
        self.assertEqual(['A', 'B', 'R', 'P', 'D', 'A'], postorder_traversal)

    def test_tree_search_success(self):
        test_tree = Tree.Tree("A")
        test_tree.insert("D")
        test_tree.insert("P")
        test_tree.insert("A")
        test_tree.insert("B")
        test_tree.insert("R")
        search_result = test_tree.search_tree("R")
        self.assertTrue(search_result)

    def test_tree_search_failure(self):
        test_tree = Tree.Tree("A")
        test_tree.insert("D")
        test_tree.insert("P")
        test_tree.insert("A")
        test_tree.insert("B")
        test_tree.insert("R")
        search_result = test_tree.search_tree("Z")
        self.assertFalse(search_result)


if __name__ == '__main__':
    unittest.main()