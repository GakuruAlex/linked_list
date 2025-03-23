from node import Node
class LinkedList:
    def __init__(self):
       self.head = None
       self.tail = None
       self.length = 0
    def __len__(self):
        return self.length
    def __str__(self):
        return f"Head:{self.head} Tail:{self.tail}"
    def __repr__(self):
            return self.__str__()
    def append(self, data):
        """_Add node at the end of linked list_

        Args:
            node (_Node_): _Node to add_
        """
        if self.head != None:
            current = self.head
            while current.next:
                current = current.next
            current._next = Node(data)
            self.tail = current.next
        else:
            self.head = Node(data)
            self.tail = self.head
        self.length += 1
    def insert(self, where: int , data):
        """_Insert a node in the linked list_

        Args:
            where (int): _Position in linked list to insert node_
            node (_Node_): _Node to insert in linked list_

        Raises:
            ValueError: _If the chain would be broken by inserting in position way off the linked list_
        """
        current = self.head
        node = Node(data)
        if where < self.length:
            for _ in range(where - 2):
                current = current.next
            after = current.next
            current._next = node
            node._next = after
            self.length += 1
        elif where == self.length + 1:
            self.append(node)
        else:
            raise ValueError("Too far from last node")

    def display(self):
        current = self.head
        while current != None:
            print(f"{current} -> ", end="")
            current = current.next
        print("None")

