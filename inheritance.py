class A:
    
    def johirul(self):
        print("johirul is a good boy")
    
        
class B (A):
   
    
    def sagor(self):
        
        #will call johirul, this function will use property of A class
        # and here A is parent class and B is child class because B use A property
        # this process is called inheritance
        print("sagor is a good boy")
        
        
   
    
t1 = B()
t1.sagor()
t1.johirul()

