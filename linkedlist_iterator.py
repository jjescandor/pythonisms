
class Node:
    """
    This is the class to create a node
    """

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values:
            for val in reversed(values):
                self.insert(val)

    def insert(self, value):
        node = Node(value)
        if self.head:
            node.next = self.head
        self.head = node

    def __iter__(self):
        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return value_generator()

    def __len__(self):
        return len([i for i in iter(self)])

    def __eq__(self, other):
        return list(self) == list(other)

if __name__ == "__main__":
    ll = LinkedList(["aloha","hello", "kumusta", "bounjour"])
    for greeting in ll:
        print(greeting)