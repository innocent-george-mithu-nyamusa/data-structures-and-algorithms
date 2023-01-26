from node import Node


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "created singly linked list"

    def createNode(self, value, location):
        if self.head is None:
            return "the head reference is none"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
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
        return "created node"

    def traversal(self):
        """the method loops through the list to find required value"""

        if self.head is None:
            print("there is nothing to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode.next == self.head:
                    break

    def search(self, nodeValue):
        if self.head is None:
            return "there is no node in singly linked list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                elif tempNode.value == self.tail.next:
                    return "the node does not exist in this singly linked list"
                tempNode = tempNode.next
    def deleteNode(self, location):
        if self.head is None:
            print("There is not any node in CSLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                
    def deleteCSLL(self):
        self.head = None
        self.tail = None


circularList = CircularLinkedList()
circularList.createSLL(12)
circularList.createNode(10, 0)
circularList.createNode(11, 0)
circularList.createNode(15, 1)
circularList.createNode(67, 2)
circularList.createNode(21, 1)

# print(circularList.search(15))
print([n.value for n in circularList])

circularList.deleteNode(0)
circularList.deleteCSLL()
print([n.value for n in circularList])