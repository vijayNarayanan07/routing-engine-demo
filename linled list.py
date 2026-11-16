class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def remove(self, value):
        if self.head is None:
            return False

        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return True

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                self.size -= 1
                return True
            current = current.next
        return False

    def find(self, value):
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head, self.tail = previous, self.head
        if self.tail is not None:
            self.tail.next = None

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __repr__(self):
        values = ", ".join(str(item) for item in self)
        return f"LinkedList([{values}])"


if __name__ == "__main__":
    numbers = LinkedList()
    for value in [10, 20, 30, 40]:
        numbers.append(value)

    numbers.prepend(5)
    print(f"List: {numbers}")
    print(f"Index of 30: {numbers.find(30)}")
    numbers.remove(20)
    print(f"After removing 20: {numbers}")
    numbers.reverse()
    print(f"Reversed: {numbers}")
    print(f"Length: {len(numbers)}")
