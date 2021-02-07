# https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/

class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None

    def add_last(self, data):
        new_node = node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def add_first(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, data):
        # first check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must in LinkedList")

        new_node = node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def length(self):
        current_node = self.head
        total = 0
        while current_node.next is not None:
            total += 1
            current_node = current_node.next
        return total

    def print_list(self):
        elems = []
        cur_node = self.head
        while cur_node:
            elems.append(cur_node.data)
            cur_node = cur_node.next

        print(elems)


lst = linked_list()

lst.add_last(0)
lst.add_last(1)
lst.add_first(4)
lst.add_first(5)
lst.insertAfter(lst.head.next, 7)
lst.print_list()
