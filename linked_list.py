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
            start = self.head
            while start.next:
                start = start.next
            start._next = Node(data)
            self.tail = start.next
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
        start = self.head
        node = Node(data)
        if where < self.length:
            for _ in range(where - 2):
                start = start.next
            after = start.next
            start._next = node
            node._next = after
            self.length += 1
        elif where == self.length + 1:
            self.append(node)
        else:
            raise ValueError("Too far from last node")
    def delete_node(self, data, start):
        if start.data == data and start == self.head:
            if start.next != None:
               self.head = start.next
            del start
            return
        if start != self.tail:
            if start.next.data == data and start.next.next != None:
                start._next = start.next.next
                del start
                return
        if start == self.tail:
            print(f"Node with {data} not found")
            return
        self.delete_node(data= data, start= start.next)

    def display(self):
        start = self.head
        while start != None:
            print(f"{start} -> ", end="")
            start = start.next
        print("None")

