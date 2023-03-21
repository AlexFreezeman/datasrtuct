from utils.stack import Stack
from utils.node import Node


def main():
    n1 = Node(5, None)
    n2 = Node('a', n1)
    print(n1.data)
    print(n2.data)
    print(n1)
    print(n2.next_node)

    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')
    print(stack.top.data)
    print(stack.top.next_node.data)
    print(stack.top.next_node.next_node.data)
    print(stack.top.next_node.next_node.next_node)


if __name__ == "__main__":
    main()
