class LinkedList:
    def __init__(self):
       self.__size = 0
       self.head = None
       self.tail = None
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, increment):
        self.__size += increment
    def __len__(self):
        return self.size
    def append(self, data):
        self.size += 1
        node = Node(data)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node
        self.tail = node
    def display(self):
        current = self.head
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print('None')
class Node():
    linked = LinkedList()
    def __init__(self, data):
        self.__next = None
        self.data = data
    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self, node_a):
        self.__next = node_a
        self.linked.size += 1
        self.linked.tail = node_a
    def __str__(self):
        return f"{self.data}"
def main()-> None:
    node = Node(2)
    node_1 = Node(4)
    linked_list = LinkedList()
    linked_list.append(node)
    linked_list.append(node_1)
    node_2 = Node(5)
    node_1.next = node_2
    print(len(linked_list))
    linked_list.display()

if __name__ =="__main__":
    main()