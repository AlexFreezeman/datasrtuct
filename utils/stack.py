from utils.node import Node


class Stack:

    def __init__(self) -> None:
        """инициализация пустого стэка"""
        # top— последний помещенный в стек элемент, хранится только он
        self.top = None

    def push(self, data) -> None:
        """добавляет элемент в  стэк"""
        node = Node(data)
        if self.top:
            node.next_node = self.top
        self.top = node

    def pop(self) -> any:
        node = self.top
        data = self.top.data
        self.top = node.next_node
        return data
