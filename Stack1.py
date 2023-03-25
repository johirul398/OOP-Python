# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:23:34 2023

@author: MD JOHIRUL ISLAM
"""

def is_empty():
    return len(items) == 0

def push():
    
    print("enter how many value you want as input : ")
    n = int(input())
    for i in range (n):
        a = int(input("enter the element of stack :"))
        items.append(a)

def pop():
    if is_empty():
        return None
    else:
        print("enter how many value you want to pop : ")
        b = int(input())
        for i in range (b):
           items.pop()

def peek():
    if is_empty():
        return None
    else:
        
        return items[-1]


items = []

print(" enter the number you want to input : ")

n = int(input())

for i in range (n):
    a = int(input())
    items.append(a)
   

push()

print(peek())

pop()

print(peek())
