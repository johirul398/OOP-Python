# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 20:04:02 2023

@author: MD JOHIRUL ISLAM
"""

class A:
    
    def __init__(self):
        print("johirul is a good boy")
    
        
class B (A):
   
    
    def __init__(self):
        
        # this is called method overriding because the function of A class 
        # is also here but as same name so the function of B class will override it
        # if we need to be call super class we cal call using super() function
        super().__init__() # call ssuper class or parent class
        print("sagor is a good boy")
        
        
   
    
t1 = B()

