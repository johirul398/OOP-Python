# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 12:17:24 2023

@author: MD JOHIRUL ISLAM
"""


def enqueue(v):
    global head
    global tail
    global capasity
    global item
    global s_point
    
    if(tail+1)%capasity ==head:
        print("queue is full")
        return
        
    if head == -1:
        head = s_point
        tail = head
        item[tail] = v
    else:
        tail = (tail+1)%capasity
        item[tail] = v
        
def dequeue():
    global head
    global tail
    global capasity
    global item
    global s_point
    
    if head ==-1:
        print("queue is empty")
        return
    item[head] = None
    if head == tail:
        head = -1
        tail = -1
    else:
        head = (head+1)%capasity
        
def front():
    print(" Afyer enqueue and dequeue the head is : ",item[head])
        
 
item = []
head = -1
tail = -1
capasity = 50
item = [None]*capasity
s_point = 0

print("enter the number of element you want to enqueue : ")
a = int(input())
i=0
while i < a:
  i = i+1
  enqueue(input())
  
print("enter how many the number of element you want to dequeue : ")
a = int(input())
i=0
while i < a:
  i = i+1
  dequeue()
  
front()




    
    
    