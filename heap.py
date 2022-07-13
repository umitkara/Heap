"""
Heap Data Structure implementation.
"""


class Heap: 
    def __init__(self): 
        self.heap_array = [] 
  
    def insert(self, key):
        """
        Inserts a key into the heap.
        """
        self.heap_array.append(key) 
        self.percolate_up(len(self.heap_array) - 1) 
  
    def percolate_up(self, index):
        """
        Moves the value at the given index up the heap.
        """
        parent = (index - 1) // 2
        if index <= 0: 
            return
        elif self.heap_array[index] < self.heap_array[parent]: 
            self.heap_array[index], self.heap_array[parent] = self.heap_array[parent], self.heap_array[index] 
            self.percolate_up(parent) 
  
    def min_child(self, index): 
        """
        Returns the index of the minimum child of the node at the given index.
        """
        if index * 2 + 1 > len(self.heap_array) - 1: 
            return index * 2
        else: 
            if self.heap_array[index*2] < self.heap_array[index*2+1]: 
                return index * 2
            else: 
                return index * 2 + 1
  
    def percolate_down(self, index): 
        """
        Moves the value at the given index down the heap.
        """
        if index * 2 + 1 > len(self.heap_array) - 1: 
            return
        child = self.min_child(index) 
        if self.heap_array[index] > self.heap_array[child]: 
            self.heap_array[index], self.heap_array[child] = self.heap_array[child], self.heap_array[index] 
            self.percolate_down(child) 
  
    def delete(self): 
        """
        Removes and returns the top value of the heap.
        """
        self.heap_array[0], self.heap_array[-1] = self.heap_array[-1], self.heap_array[0] 
        self.heap_array.pop() 
        self.percolate_down(0)
        

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
    print(heap.heap_array)
    print(heap.min_child(3))