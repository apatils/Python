'''
    Program to create linkedList
'''

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    two = Node(2)
    three = Node(3)
    llist.head.next = two
    two.next = three
    llist.print_list()    