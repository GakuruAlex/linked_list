class LinkedList:
    size = 0
    def __init__(self):
       self.head = None
       self.tail = None
    def __len__(self):
        return self.size
    def __str__(self):
        return f"Head: {self.head} Tail:{self.tail}"
    def __repr__(self):
            return self.__str__()
    def append(self, node):
        """_Add node at the end of linked list_

        Args:
            node (_Node_): _Node to add_
        """
        last = self.tail
        last.next = node
        self.tail = node
    def insert(self, where: int , node):
        """_Insert a node in the linked list_

        Args:
            where (int): _Position in linked list to insert node_
            node (_Node_): _Node to insert in linked list_

        Raises:
            ValueError: _If the chain would be broken by inserting in position way off the linked list_
        """
        current = self.head
        if where < len(self):
            for _ in range(where - 2):
                current = current._next
            after = current._next
            current._next = node
            node._next = after
        elif where == len(self):
            self.append(node)
        else:
            raise ValueError("Too far from last node")
    def display(self):
        current = self.head
        while current != None:
            print(f"{current} -> ", end="")
            current = current.next
        print("None")
    class Node():
        def __init__(self, linked_list, data):
            self._next = None
            self.linked_list = linked_list
            if linked_list.size == 0:
                linked_list.head = self
            self.data = data
            LinkedList.size +=1
        @property
        def next(self):
            return self._next
        @next.setter
        def next(self, node_a):
                if self.next == None:
                    self.linked_list.tail = node_a
                    self._next = node_a
                else:
                    next_node = self._next
                    self._next = node_a
                    node_a._next =  next_node
        def __str__(self):
            return f"{self.data}"
        def __repr__(self):
            return self.__str__()
def main()-> None:
    linked_list = LinkedList()
    print(len(linked_list))
    node_1 = LinkedList.Node(linked_list, 2)
    node_2 = LinkedList.Node(linked_list, 4)
    print(len(linked_list))
    node_3 = LinkedList.Node(linked_list, 5)
    node_1.next = node_2
    node_2.next = node_3
    node_4 = LinkedList.Node(linked_list, 7)
    node_3.next = node_4
    node_5 = LinkedList.Node(linked_list, 10)
    node_4.next = node_5
    linked_list.append(LinkedList.Node(linked_list , 12))
    print(linked_list)
    linked_list.display()
    print(len(linked_list))
    linked_list.insert(5, LinkedList.Node(linked_list, 8))
    linked_list.display()

if __name__ =="__main__":
    main()