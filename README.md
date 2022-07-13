# Heap

In this repo i tried to implement the heap data structure in python with different methods.

A heap is a binary tree where the value of each node is greater than(less than) or equal to the values of its children. There are 2 types of heaps:
- Min Heap
- Max Heap

Both of their strucure are mostly same. The difference is min heap has the smallest value at the root and max heap has the largest value at the root.

There are 3 main methods to implement a heap:
- Insert
- Peek
- Top

The insert method is used to add a new element to the heap. The peek method is used to get the value of the root element. The top method is used to get the value of the root element and remove it from the heap.

With these main methods we can implement the following methods:
- Remove
- Increase Key
- Meld

The remove method is used to remove the given element from the heap. The increase key method is used to increase the value of the given element. The meld method is used to merge two heaps.


There are many types of heaps:
- Binary Heap
- D-ary Heap
- 2–3 heap
- Leftist Heap
- Ternary Heap
- Binomial Heap
- Fibonacci Heap
- Treap

## Performance

I treid to implement binary heap. So here is the theoretic bounds of the binary heap:

- **Insert**: O(log n)
- **Peek**: O(1)
- **Top**: O(log n)
- **Remove**: O(log n) \*
- **Increase Key**: O(log n) \*
- **Meld**: O(n) \*

\* Not implemented.