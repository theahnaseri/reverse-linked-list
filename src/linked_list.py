from termcolor import colored

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print_linked_list(self):
        current = self.head
        while current is not None:
            if current.next is not None:
                print(colored(f"{current.value}|{current.next.value} -> ", color="blue"), end="")
            else:
                print(colored(current.value, color="blue"))
            current = current.next