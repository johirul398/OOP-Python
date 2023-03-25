class student:
    id = ""
    gpa = ""
    
    
    def __init__(self, a, b):
        self.id = a
        self.gpa = b
    
    def display(self):
        print(f"id : {self.id}, gpa  : {self.gpa}")
        
    
    
johirul = student(30073547, 4.00)
johirul.display()

