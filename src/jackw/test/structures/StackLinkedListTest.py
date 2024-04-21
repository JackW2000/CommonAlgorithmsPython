import unittest

from src.jackw.main.structures.StackLinkedList import Stack


class LinkedListTest(unittest.TestCase):
    def test_stack_initialise_empty(self):
        test_stack = Stack()
        self.assertEqual("Sorry, the stack is currently empty!", test_stack.peek())

    def test_stack_initialise(self):
        test_stack = Stack()
        self.assertEqual("10 has been successfully added to the top stack.", test_stack.push(10))
        self.assertEqual("10 is on top of the stack.", test_stack.peek())

    def test_stack_push(self):
        test_stack = Stack()
        self.assertEqual("10 has been successfully added to the top stack.", test_stack.push(10))
        self.assertEqual("20 has been successfully added to the top stack.", test_stack.push(20))
        self.assertEqual("30 has been successfully added to the top stack.", test_stack.push(30))
        self.assertEqual("40 has been successfully added to the top stack.", test_stack.push(40))

    def test_stack_pop(self):
        test_stack = Stack()
        self.assertEqual("10 has been successfully added to the top stack.", test_stack.push(10))
        self.assertEqual("20 has been successfully added to the top stack.", test_stack.push(20))
        self.assertEqual("30 has been successfully added to the top stack.", test_stack.push(30))
        self.assertEqual("40 has been successfully added to the top stack.", test_stack.push(40))
        self.assertEqual("40 has been removed from the top of the stack.", test_stack.pop())
        self.assertEqual("30 has been removed from the top of the stack.", test_stack.pop())

    def test_stack_display(self):
        test_stack = Stack()
        self.assertEqual("10 has been successfully added to the top stack.", test_stack.push(10))
        self.assertEqual("20 has been successfully added to the top stack.", test_stack.push(20))
        self.assertEqual("30 has been successfully added to the top stack.", test_stack.push(30))
        self.assertEqual("40 has been successfully added to the top stack.", test_stack.push(40))
        self.assertEqual("40 has been removed from the top of the stack.", test_stack.pop())
        self.assertEqual("30 has been removed from the top of the stack.", test_stack.pop())
        self.assertEqual("Position 0 holds 20\nPosition 1 holds 10\n", test_stack.display())

    def test_stack_get_length(self):
        test_stack = Stack()
        self.assertEqual("10 has been successfully added to the top stack.", test_stack.push(10))
        self.assertEqual("20 has been successfully added to the top stack.", test_stack.push(20))
        self.assertEqual("30 has been successfully added to the top stack.", test_stack.push(30))
        self.assertEqual("40 has been successfully added to the top stack.", test_stack.push(40))
        self.assertEqual("The stack is 4 nodes long.", test_stack.get_length())


if __name__ == '__main__':
    unittest.main()
