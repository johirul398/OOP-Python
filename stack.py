# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 14:59:58 2023

@author: MD JOHIRUL ISLAM
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self):
        
        print("enter how many value you want as input : ")
        n = int(input())
        for i in range (n):
            a = int(input("enter the element of stack :"))
            self.items.append(a)

    def pop(self):
        if self.is_empty():
            return None
        else:
            print("enter how many value you want to pop : ")
            b = int(input())
            for i in range (b):
               self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        else:
            
            return self.items[-1]

    def size(self):
        return len(self.items)

stack = Stack()

stack.push()

print(stack.peek())

stack.pop()

print(stack.peek())

print(stack.size())
