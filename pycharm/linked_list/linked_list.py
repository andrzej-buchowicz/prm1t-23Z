class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        curr_elem = self.head
        num_elem = 0
        while curr_elem is not None:
            num_elem += 1
            curr_elem = curr_elem.next
        return num_elem

    def append(self, elem):
        assert isinstance(elem, Element)
        assert elem.next is None

        if self.head is None:
            self.head = elem
            return

        curr_elem = self.head
        while True:
            if curr_elem.next is None:
                break
            curr_elem = curr_elem.next
        curr_elem.next = elem

    def __getitem__(self, index):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def find(self, elem):
        return -1






