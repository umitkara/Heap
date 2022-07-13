"""
Create a heap implementation in python.

The class needs to implement the following methods:

insert(value)
peek()
pop()

The class needs to implement the following properties:

size
"""
from typing import Callable


class Heap:
    def __init__(self, comparator: Callable[[int, int], bool]=lambda x, y: x < y):
        self.size = 0
        self.heap = []
        self.comparator = comparator

    def insert(self, value):
        """
        Inserts a value into the heap.
        """
        self.heap.append(value)
        self.size += 1
        self.__up_heapify(self.size - 1)

    def peek(self):
        """
        Returns the top value of the heap.
        """
        if self.size == 0:
            return None
        return self.heap[0]

    def pop(self) -> int:
        """
        Removes and returns the top value of the heap.
        """
        if self.size == 0:
            return None
        self.__swap(0, self.size - 1)
        value = self.heap.pop()
        self.size -= 1
        self.__down_heapify(0)
        return value

    def __swap(self, idx1, idx2):
        """
        Swaps the values at the given indices.
        """
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def __up_heapify(self, idx):
        """
        Moves the value at the given index up the heap.
        """
        if idx == 0:
            return
        parent_idx = (idx - 1) // 2
        if self.comparator(self.heap[idx], self.heap[parent_idx]):
            self.__swap(parent_idx, idx)
            self.__up_heapify(parent_idx)

    def __down_heapify(self, idx):
        """
        Moves the value at the given index down the heap.
        """
        if idx < 0 or idx > self.size - 1:
            return
        left_child_idx = idx * 2 + 1
        right_child_idx = idx * 2 + 2
        if left_child_idx > self.size - 1:
            return
        if right_child_idx > self.size - 1:
            if self.comparator(self.heap[left_child_idx], self.heap[idx]):
                self.__swap(left_child_idx, idx)
                self.__down_heapify(left_child_idx)
            return
        smallest_idx = left_child_idx if self.comparator(self.heap[left_child_idx], self.heap[right_child_idx]) else right_child_idx
        if self.comparator(self.heap[smallest_idx], self.heap[idx]):
            self.__swap(smallest_idx, idx)
            self.__down_heapify(smallest_idx)


if __name__ == "__main__":
    heap = Heap()
    heap.insert(10)
    heap.insert(8)
    heap.insert(9)
    heap.insert(11)
    heap.insert(3)
    heap.insert(2)
    heap.insert(1)
    heap.insert(4)
    heap.insert(5)
    heap.insert(0)
    heap.insert(12)
    heap.insert(13)
    heap.insert(14)
    heap.insert(15)
    heap.insert(16)
    heap.insert(17)
    print(heap.heap)
    print(heap.pop())
    print(heap.pop())
    print(heap.heap)