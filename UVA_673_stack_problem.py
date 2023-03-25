# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 01:30:22 2023

@author: MD JOHIRUL ISLAM
"""
def check(n):

    items = []
    for i  in n:
        if i in "[(":
            items.append(i)
        else:
            if len(items) == 0:
                return "No"
            p = items.pop()
            if (i == ")" and p!= "(") or (i == "]" and p!= "["):
                return "No"
    if len(items) > 0:
        return "No"
    return "Yes"
            

    



a = int(input())
i=0
while i < a:
  i = i+1
  print(check(input()))
    