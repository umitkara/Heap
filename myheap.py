from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class HeapNode:
    data: Any
    priority: int
    left: Optional[HeapNode] = None
    right: Optional[HeapNode] = None
    leaf: bool = False
    
    def __lt__(self, other: HeapNode):
        return self.priority < other.priority
    
    def __eq__(self, other: HeapNode):
        return self.priority == other.priority
    
    def __gt__(self, other: HeapNode):
        return self.priority > other.priority
    
    def __le__(self, other: HeapNode):
        return self.priority <= other.priority
    
    def __ge__(self, other: HeapNode):
        return self.priority >= other.priority

    def __ne__(self, other: HeapNode):
        return self.priority != other.priority
    
    def __str__(self) -> str:
        return str(self.data) + " " + str(self.priority)


class MaxHeap:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self, data:Any, priority:int):
        """
        Inserts a new node into the heap.
        """
        self.size += 1
        node = HeapNode(data, priority)
        if self.root is None:
            self.root = node
        else:
            self.root = self.__insert(self.root, node)
    
    def __insert(self, root: HeapNode, node: HeapNode):
        """
        Insert helper function.
        """
        if root.priority > node.priority:
            if root.right is None:
                root.right = node
                return root
            else:
                root.right = self.__insert(root.right, node)
                return root
        else:
            if root.left is None:
                root.left = node
                return root
            else:
                root.left = self.__insert(root.left, node)
                return root
    
    def delete(self):
        """
        Deletes the root node of the heap.
        """
        if self.root is None:
            return None
        else:
            self.size -= 1
            return self.__delete(self.root)
    
    def __delete(self, root: HeapNode):
        """
        Delete helper function.
        """
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            root.data, root.priority = self.__find_max(root.left)
    
    def __find_max(self, root: HeapNode):
        """
        Finds the maximum value in the heap.
        """
        if root.right is None:
            return root.data, root.priority
        else:
            return self.__find_max(root.right)
    
    def __str__(self):
        return str(self.root)
    
    def print_tree(self):
        self.__print_tree(self.root)
        
    def __print_tree(self, root:HeapNode):
        if root is None:
            return
        else:
            self.__print_tree(root.left)
            print(root.data, root.priority)
            self.__print_tree(root.right)
    
    def peak(self):
        return self.root.data

if __name__ == "main":
    h = MaxHeap()
    h.insert(1, 1)
    h.insert(2, 2)
    h.insert(3, 3)
    h.insert(4, 4)
    h.insert(5, 1)
    h.print_tree()