from linked_list import LinkedList
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