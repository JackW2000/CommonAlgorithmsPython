import unittest

from src.jackw.main.structures.QueueArray import Queue


class LinkedListTest(unittest.TestCase):
    def test_queue_initialise_empty(self):
        test_queue = Queue()
        self.assertEqual(0, test_queue.get_head())
        self.assertEqual(0, test_queue.get_tail())
        self.assertEqual(0, test_queue.get_max_len())

    def test_queue_initialise(self):
        test_queue = Queue(10)
        self.assertEqual(0, test_queue.get_head())
        self.assertEqual(10, test_queue.get_value(test_queue.get_head()))
        self.assertEqual(0, test_queue.get_tail())
        self.assertEqual(10, test_queue.get_value(test_queue.get_head()))
        self.assertEqual(10, test_queue.get_max_len())

    def test_queue_enqueue(self):
        test_queue = Queue(10)
        test_queue.enqueue(20)
        test_queue.enqueue(30)
        test_queue.enqueue(40)
        self.assertEqual(0, test_queue.get_head())
        self.assertEqual(10, test_queue.get_value(test_queue.get_head()))
        self.assertEqual(3, test_queue.get_tail())
        self.assertEqual(40, test_queue.get_value(test_queue.get_tail()))
        self.assertEqual(10, test_queue.get_max_len())

    def test_queue_dequeue(self):
        test_queue = Queue(10)
        test_queue.enqueue(20)
        test_queue.enqueue(30)
        test_queue.enqueue(40)
        test_queue.dequeue()
        test_queue.dequeue()
        test_queue.dequeue()
        self.assertEqual(0, test_queue.get_head())
        self.assertEqual(40, test_queue.get_value(test_queue.get_head()))
        self.assertEqual(0, test_queue.get_tail())
        self.assertEqual(40, test_queue.get_value(test_queue.get_tail()))
        self.assertEqual(10, test_queue.get_max_len())

    def test_queue_peek(self):
        test_queue = Queue(10)
        test_queue.enqueue(20)
        test_queue.enqueue(30)
        test_queue.enqueue(40)
        self.assertEqual("10 is at the front of the queue.", test_queue.peek())

    def test_queue_display(self):
        test_queue = Queue(10)
        test_queue.enqueue(20)
        test_queue.enqueue(30)
        test_queue.enqueue(40)
        self.assertEqual("Position 0 holds 10\nPosition 1 holds 20\nPosition 2 holds 30\n", test_queue.display())


if __name__ == '__main__':
    unittest.main()
