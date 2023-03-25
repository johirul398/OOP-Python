# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 23:44:17 2023

@author: MD JOHIRUL ISLAM
"""

queue = []
while True:
    a = int(input())
    if a == 0:
        break
    
    for i in range(1, a+1):
        queue.append(i)
        
    print("Discarded cards:")
    
    while True:
        if len(queue) == 1:
            print("\n")
            break
        if len(queue) == 2:
            print(" ",queue[0])
            queue.pop(0)
            
        else:
            print(f" {queue[0]},")
            #print(queue[0])
            queue.pop(0)
            s = queue[0]
            queue.pop(0)
            queue.append(s)
            
    print("Remaining card: \n",queue[0])
    queue.pop(0)
            
            
            
            
            
            
            