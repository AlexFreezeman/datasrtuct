import unittest
from utils.custom_queue import Queue
from utils.node import Node


class test_queue(unittest.TestCase):
    def test__init__(self):
        queue = Queue()
        self.assertIsNone(queue.head)
        self.assertIsNone(queue.tail)

    def test_enqueue(self):
#        node_10 = Node(10)
#        node_20 = Node(20)
#        node_30 = Node(30)
#        node_40 = Node(40)
        queue = Queue()
        queue.enqueue("data1")
        queue.enqueue("data2")
        queue.enqueue("data3")
        queue.enqueue("data4")
        self.assertIs(queue.head.data, "data1")
        self.assertIs(queue.head.next_node.data, "data2")
        self.assertIs(queue.tail.data, "data4")
        self.assertIsNone(queue.tail.next_node)

