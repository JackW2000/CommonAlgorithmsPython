import unittest

from src.jackw.main.structures.QueueLinkedList import Queue


class LinkedListTest(unittest.TestCase):
    def test_queue_initialise(self):
        test_queue = Queue()
        self.assertIsNone(test_queue.get_head())
        self.assertIsNone(test_queue.get_tail())

    def test_queue_enqueue(self):
        test_queue = Queue()
        test_queue.enqueue(10)
        test_queue.enqueue(20)
        test_queue.enqueue(30)
        self.assertEqual(10, test_queue.get_head().get_data())
        self.assertEqual(30, test_queue.get_tail().get_data())
        self.assertEqual(3, test_queue.get_length())

    def test_queue_dequeue(self):
        test_queue = Queue()
        test_queue.enqueue(10)
        test_queue.enqueue(20)
        test_queue.enqueue(30)
        test_queue.dequeue()
        test_queue.dequeue()
        self.assertEqual(30, test_queue.get_head().get_data())
        self.assertEqual(30, test_queue.get_tail().get_data())
        self.assertEqual(1, test_queue.get_length())

    def test_queue_peek(self):
        test_queue = Queue()
        test_queue.enqueue(10)
        test_queue.enqueue(20)
        test_queue.enqueue(30)
        self.assertEqual("10 is at the front of the queue.", test_queue.peek())

    def test_queue_display(self):
        test_queue = Queue()
        test_queue.enqueue(10)
        test_queue.enqueue(20)
        test_queue.enqueue(30)
        self.assertEqual("Position 0 holds 10\nPosition 1 holds 20\nPosition 2 holds 30\n", test_queue.display())


if __name__ == '__main__':
    unittest.main()
