from utils.node import Node


class Stack():

    def __init__(self) -> None:
        """инициализация пустого стэка"""
        self.elements = []
        # top— последний помещенный в стек элемент
        self.top = None

    def push(self, data) -> Node:
        """добавляет элемент в  стэк и возвращает его"""
        if len(self.elements) == 0:
            new_node = Node(data)
        else:
            new_node = Node(data, self.top)
        self.top = new_node
        return self.elements.append(new_node)

    def pop(self) -> Node:
        """удаляет последний элемент из стэка и возвращает его данные"""
        if len(self.elements) == 1:
            last_node = self.top
            self.elements.pop()
            self.top = None
            return last_node.data
        elif len(self.elements) > 1:
            last_node = self.top
            self.top = self.elements[len(self.elements) - 2]
            self.elements.pop()
            return last_node.data
        else:
            self.top = None
            return None
