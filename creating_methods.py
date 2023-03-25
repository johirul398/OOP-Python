class student:
    id = ""
    gpa = ""
    
    
    def set_v(self, a, b):
        self.id = a
        self.gpa = b
    
    def display(self):
        print(f"id : {self.id}, gpa  : {self.gpa}")
        
    
    
johirul = student()
johirul.set_v(30073547, 4.00)
johirul.display()

