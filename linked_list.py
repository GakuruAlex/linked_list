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
    class Node():
        def __init__(self, linked_list, data):
            self._next = None
            if linked_list.size == 0:
                linked_list.head = self
            self.data = data
            LinkedList.size +=1
        @property
        def next(self):
            return self._next
        @next.setter
        def next(self, node_a):
                self._next = node_a
                LinkedList.tail = node_a
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
    print(linked_list)
    print(len(linked_list))

if __name__ =="__main__":
    main()