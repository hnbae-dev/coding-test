
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        
    def append(self, value):
        prev_node = self.head
        new_node = Node(value)
        while prev_node.next is not None:
            prev_node = prev_node.next
        prev_node.next = new_node
        
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
    
    def get_node(self, index):
        cur = self.head
        cur_index = 0
        while cur_index < index:
            cur = cur.next
            cur_index += 1
        return cur

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)

print(linked_list.get_node(2).data)
