import unittest
from src.jackw.main.structures import LinkedList
from src.jackw.main.structures.LinkedList import Node


class LinkedListTest(unittest.TestCase):
    def test_linked_list_initialise_empty(self):
        test_linked_list = LinkedList.DoubleLinkedList()
        self.assertIsNone(test_linked_list.get_head())
        self.assertIsNone(test_linked_list.get_tail())
        self.assertEqual(0, test_linked_list.total_nodes)

    def test_linked_list_initialise(self):
        test_linked_list = LinkedList.DoubleLinkedList(Node(10))
        self.assertEqual(10, test_linked_list.get_head().get_data())
        self.assertEqual(10, test_linked_list.get_tail().get_data())
        self.assertEqual(1, test_linked_list.total_nodes)

    def test_linked_list_append_single_value(self):
        test_linked_list = LinkedList.DoubleLinkedList(Node(10))
        test_linked_list.append(Node(20))
        self.assertEqual(10, test_linked_list.get_head().get_data())
        self.assertEqual(20, test_linked_list.get_tail().get_data())
        self.assertEqual(2, test_linked_list.total_nodes)

    def test_linked_list_append_multiple_values(self):
        test_linked_list = LinkedList.DoubleLinkedList(Node(10))
        test_linked_list.append(Node(20))
        test_linked_list.append(Node(30))
        test_linked_list.append(Node(40))
        test_linked_list.append(Node(50))
        self.assertEqual(10, test_linked_list.get_head().get_data())
        self.assertEqual(50, test_linked_list.get_tail().get_data())
        self.assertEqual(50, test_linked_list.get_tail().get_data())
        self.assertEqual(5, test_linked_list.total_nodes)

    def test_linked_list_insert_single_value(self):
        test_linked_list = LinkedList.DoubleLinkedList(Node(10))
        test_linked_list.insert(Node(20), 0)
        self.assertEqual(20, test_linked_list.get_head().get_data())
        self.assertEqual(10, test_linked_list.get_tail().get_data())
        self.assertEqual(2, test_linked_list.total_nodes)

    def test_linked_list_insert_multiple_values(self):
        test_linked_list = LinkedList.DoubleLinkedList(Node(10))
        test_linked_list.insert(Node(20), 1)
        test_linked_list.insert(Node(30), 2)
        test_linked_list.insert(Node(40), 3)
        test_linked_list.insert(Node(50), 4)
        self.assertEqual(10, test_linked_list.get_head().get_data())
        self.assertEqual(50, test_linked_list.get_tail().get_data())
        self.assertEqual(5, test_linked_list.total_nodes)

    def test_linked_list_remove_single_value(self):
        test_linked_list = LinkedList.DoubleLinkedList(Node(10))
        test_linked_list.append(Node(20))
        test_linked_list.remove(0)
        self.assertEqual(20, test_linked_list.get_head().get_data())
        self.assertEqual(20, test_linked_list.get_tail().get_data())
        self.assertEqual(1, test_linked_list.total_nodes)

    def test_linked_list_remove_multiple_values(self):
        test_linked_list = LinkedList.DoubleLinkedList(Node(10))
        test_linked_list.append(Node(20))
        test_linked_list.append(Node(30))
        test_linked_list.append(Node(40))
        test_linked_list.append(Node(50))
        test_linked_list.remove(0)
        test_linked_list.remove(0)
        test_linked_list.remove(0)
        self.assertEqual(40, test_linked_list.get_head().get_data())
        self.assertEqual(50, test_linked_list.get_tail().get_data())
        self.assertEqual(2, test_linked_list.total_nodes)

    def test_linked_list_size_empty(self):
        test_linked_list = LinkedList.DoubleLinkedList()
        self.assertEqual(None, test_linked_list.get_head())
        self.assertEqual(None, test_linked_list.get_tail())
        self.assertEqual(0, test_linked_list.size())

    def test_linked_list_size_multiple_items(self):
        test_linked_list = LinkedList.DoubleLinkedList(Node(10))
        test_linked_list.append(Node(20))
        test_linked_list.append(Node(30))
        test_linked_list.append(Node(40))
        test_linked_list.append(Node(50))
        self.assertEqual(10, test_linked_list.get_head().get_data())
        self.assertEqual(50, test_linked_list.get_tail().get_data())
        self.assertEqual(5, test_linked_list.size())

    def test_linked_list_search_for_not_found(self):
        test_linked_list = LinkedList.DoubleLinkedList(Node(10))
        test_linked_list.append(Node(20))
        test_linked_list.append(Node(30))
        test_linked_list.append(Node(40))
        test_linked_list.append(Node(50))
        self.assertIsNone(test_linked_list.search_for(100))

    def test_linked_list_search_for_found(self):
        test_linked_list = LinkedList.DoubleLinkedList(Node(10))
        test_linked_list.append(Node(20))
        test_linked_list.append(Node(30))
        test_linked_list.append(Node(40))
        test_linked_list.append(Node(50))
        self.assertEqual(2, test_linked_list.search_for(30))


if __name__ == '__main__':
    unittest.main()
