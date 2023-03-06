
class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None


class LinkedList:
    def __init__(self):
        self.Head = None

    def printlist(self):
        temp = self.Head
        while (temp):
            print(temp.data)
            temp = temp.Next

# Main function starts
if __name__ == '__main__':
    # list is Object of linkedlist class 
    list = LinkedList()
    list.Head = Node(1)
    second = Node(4)
    third = Node(5)

    list.Head.Next = second
    second.Next = third
    list.printlist()
