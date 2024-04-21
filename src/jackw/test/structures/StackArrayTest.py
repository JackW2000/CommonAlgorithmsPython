import unittest

from src.jackw.main.structures.StackArray import Stack


class LinkedListTest(unittest.TestCase):
    def test_stack_initialise_empty(self):
        test_stack = Stack()
        self.assertEqual("Sorry, the stack is currently empty!", test_stack.peek())

    def test_stack_initialise(self):
        test_stack = Stack(10)
        self.assertEqual("10 is on top of the stack.", test_stack.peek())

    def test_stack_push(self):
        test_stack = Stack(10)
        self.assertEqual("20 has been successfully added to the top stack.", test_stack.push(20))
        self.assertEqual("30 has been successfully added to the top stack.", test_stack.push(30))
        self.assertEqual("40 has been successfully added to the top stack.", test_stack.push(40))
        self.assertEqual("50 has been successfully added to the top stack.", test_stack.push(50))

    def test_stack_pop(self):
        test_stack = Stack(10)
        self.assertEqual("20 has been successfully added to the top stack.", test_stack.push(20))
        self.assertEqual("30 has been successfully added to the top stack.", test_stack.push(30))
        self.assertEqual("40 has been successfully added to the top stack.", test_stack.push(40))
        self.assertEqual("50 has been successfully added to the top stack.", test_stack.push(50))
        self.assertEqual("50 has been removed from the top of the stack.", test_stack.pop())
        self.assertEqual("40 has been removed from the top of the stack.", test_stack.pop())

    def test_stack_display(self):
        test_stack = Stack(10)
        self.assertEqual("20 has been successfully added to the top stack.", test_stack.push(20))
        self.assertEqual("30 has been successfully added to the top stack.", test_stack.push(30))
        self.assertEqual("40 has been successfully added to the top stack.", test_stack.push(40))
        self.assertEqual("50 has been successfully added to the top stack.", test_stack.push(50))
        self.assertEqual("50 has been removed from the top of the stack.", test_stack.pop())
        self.assertEqual("40 has been removed from the top of the stack.", test_stack.pop())
        self.assertEqual("Position 0 holds 30\nPosition 1 holds 20\n", test_stack.display())


if __name__ == '__main__':
    unittest.main()
