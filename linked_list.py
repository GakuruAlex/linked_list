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
        print(self.length)
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
    # def delete_node(self, data):
    #     node = Node(data)
    #     current = self.head
    #     if current is node and self.head._next != None:
    #         self.head = current._next
    #         del node
    #     else:
    #         while current.next != None:
    #             if current.next is node and current.next.next != None:
    #                 after = current.next
    #                 current._next = after.next
    #                 print("Deleting node ", node)
    #                 del node
    #                 self.size -= 1
    #                 print("Deleted node")
    #                 break
    #             elif current.next is node and current._next.next == None:
    #                 current.next = None
    #                 print("Deleting node", node)
    #                 self.size -= 1
    #                 del node
    #                 print("Deleted node", node)
    #                 break
    #             current = current.next

    def display(self):
        current = self.head
        while current != None:
            print(f"{current} -> ", end="")
            current = current.next
        print("None")
class Node():
        def __init__(self,  data):
            self._next = None
            self.data = data
        @property
        def next(self):
            return self._next
        def __str__(self):
            return f"{self.data}"
        def __repr__(self):
            return self.__str__()

def main()-> None:
    linked_list = LinkedList()
    print(f"Len of linked list is {len(linked_list)}")
    linked_list.append(12)
    print(linked_list)
    linked_list.display()
    linked_list.append(10)
    print(f"Len of linked list is {len(linked_list)}")
    linked_list.insert(3, 8)
    print(f"Len of linked list after insert is {len(linked_list)}")
    linked_list.display()
    linked_list.append(4)
    #linked_list.delete_node(node_4)
    linked_list.display()
    print(f"Len of linked list is after deleting node is {len(linked_list)}")
    linked_list.insert(2, 24)
    linked_list.display()

if __name__ =="__main__":
    main()