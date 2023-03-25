# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:28:31 2023

@author: MD JOHIRUL ISLAM
"""

class queue:
    def __init__(self):
        self.items = []
        
    def c_empty(self):
        return not bool(self.items)
    
    def enqueue(self, a):
        self.items.append(a)
        
    def dequeue(self):
        if not self.c_empty():
            return self.items.pop(0)


q = queue()

q.enqueue("sagor")
q.enqueue("nodi")

print(q.dequeue())