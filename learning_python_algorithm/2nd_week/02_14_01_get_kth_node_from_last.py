class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
        
    def get_node(self, index):
        count = index
        cur = self.head
        while count > 0:
            cur = cur.next
            count -= 1
        return cur

    def get_kth_node_from_last(self, k):
        length_of_list = get_length_of_linked_list(self)
        index = length_of_list - k
        kth_node = self.get_node(index)
        return kth_node
    
    
def get_length_of_linked_list(linked_list):
    length = 0
    cur = linked_list.head
    while cur is not None:
        cur = cur.next
        length += 1
    return length

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!


