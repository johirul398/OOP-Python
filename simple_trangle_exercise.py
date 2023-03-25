class t:
    b = ""
    h = ""
    
    
    def __init__(self, b, h):
        self.b = b
        self.h = h
        
        
    def area(self):
        ar = 0.5*self.b*self.h
        print(f"Area : {ar}")
    
    
        
    
    
t1 = t(12,20)
t1.area()
t2 = t(20,30)
t2.area()

