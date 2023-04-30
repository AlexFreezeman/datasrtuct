from utils.node import Node


class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        new_node = Node(data=data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self) -> None:
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next_node
        if self.head is None:
            self.tail = None
        return removed_data
