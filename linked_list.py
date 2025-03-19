class LinkedList:
    def __init__(self):
       self.size = 0
       self.head = None
       self.tail = None
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
    def __init__(self, data):
        self.next = None
        self.data = data
    def __str__(self):
        return f"{self.data}"
def main()-> None:
    node = Node(2)
    node_1 = Node(4)
    node_2 = Node(5)
    node_1.next = node_2
    linked_list = LinkedList()
    linked_list.append(node)
    linked_list.append(node_1)
    print(len(linked_list))
    linked_list.display()

if __name__ =="__main__":
    main()