
import unittest
from utils.node import Node
from utils.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = Stack()

    def tearDown(self) -> None:
        self.stack.top = None

    def test_push(self):
        self.stack.push('data_1')
        self.stack.push('data_2')

        self.assertEqual(self.stack.top.data, 'data_2')
        self.assertEqual(self.stack.top.next_node.data, 'data_1')

    def test_pop(self):
        self.stack.push('data_1')
        self.stack.push('data_2')

        self.assertEqual(self.stack.pop(), 'data_2')
        self.assertEqual(self.stack.pop(), 'data_1')

    def test_empty_stack(self):
        self.stack.push('data_1')

        self.assertEqual(self.stack.pop(), 'data_1')
        with self.assertRaises(AttributeError):
            self.stack.pop()
