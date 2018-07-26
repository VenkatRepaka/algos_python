class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert at the beginning
    def push(self, new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node

    def insert_after(self, prev_node, new_data):
        if prev_node is Node:
            print('Error')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(new_data)

    def delete(self, del_data):
        if self.head is not None:
            if self.head.data == del_data:
                self.head = self.head.next
                return
        if self.head is None:
            return
        temp = self.head
        while temp is not None:
            if temp.data == del_data:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def delete_list(self):
        temp = self.head
        while temp is not None:
            del temp.data
            current = temp
            temp = temp.next
            current.next = None
        self.head = None

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def get_count(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def find_node_iterative(self, data):
        if self.head is None:
            return False
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def find_node_recursive(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        else:
            return self.find_node_recursive(node.next, data)

    def find_nth_item(self, pos):
        temp = self.head
        count = 0
        while temp is not None:
            if count == pos:
                return temp.data
            temp = temp.next
            count += 1
        return None


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(4)
    linked_list.insert_after(linked_list.head.next.next, 2.5)
    linked_list.append(0)
    linked_list.print()
    print('Addition complete')
    linked_list.delete(2.5)
    linked_list.delete(4)
    linked_list.delete(0)
    linked_list.print()
    print('No of items in linked list {0}'.format(linked_list.get_count()))
    linked_list.delete_list()
    linked_list.print()
    print('Deleted linked list')
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.push(4)
    print('Item found {0}'.format(linked_list.find_node_iterative(1)))
    print('Item found {0}'.format(linked_list.find_node_recursive(linked_list.head, 7)))
    pos = 10
    nth_pos_item = linked_list.find_nth_item(pos)
    print('Item at {0} th position is {1}'.format(pos, 'No item' if nth_pos_item is None else nth_pos_item))
