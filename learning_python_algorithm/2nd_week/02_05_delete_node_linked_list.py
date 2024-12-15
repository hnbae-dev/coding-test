
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
    
    def add_node(self, index, value):
        new_node =  Node(value)
        
        # index가 0일 때
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = self.get_node(index - 1)
            next_node = prev_node.next
            prev_node.next = new_node
            new_node.next = next_node
            
    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            prev_node = self.get_node(index - 1)
            prev_node.next = prev_node.next.next

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.add_node(1, 6)
linked_list.add_node(0, 9)
linked_list.print_all()
print("----------")
linked_list.delete_node(0)
linked_list.print_all()

