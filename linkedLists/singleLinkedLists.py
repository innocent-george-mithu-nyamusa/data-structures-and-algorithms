from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def traverse(self):
        if self.head is not None:
            print("The singly Linked list does not exist")
        else:
            node = self.head

            while node is not None:
                print(node.value)
                node = node.next

    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                newNode.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

        def index(self, nodeValue):
            node = self.head

            if node is None:
                print("Linked Linst does not exist")
            else:
                while node is not None:
                    if node.value == nodeValue:
                        return node.value
                    node = node.next
                return "value does not exist"

        def delList(self):
            if self.head is None:
                print("singley linked list does not exist")
            else:
                self.head = None
                self.tail = None

        def deleteNode(self, location):
            if self.head is None:
                print("Singly linked list does not exist")
            else:
                if location == 0:
                    if self.head == self.tail:
                        self.head = None
                        self.tail = None
                    else:
                        self.head = self.head.next
                elif location == 1:
                    if self.head == self.tail:
                        self.head = None
                        self.tail = None
                    else:
                        node = self.head
                        while node is not None:
                            if node.next == self.tail:
                                break
                            node = node.next
                        node.next = None
                        self.tail = node
                else:
                    tempNode = self.head
                    index = 0
                    while index < location - 1:
                        tempNode = tempNode.next
                        index += 1
                    nextNode = tempNode.next
                    tempNode.next = nextNode.next


singleLinkedList = LinkedList()

singleLinkedList.insert(12, 1)
singleLinkedList.insert(23, 1)
singleLinkedList.insert(82, 1)
singleLinkedList.insert(55, 2)
singleLinkedList.insert(12, 2)
print([node.value for node in singleLinkedList])
