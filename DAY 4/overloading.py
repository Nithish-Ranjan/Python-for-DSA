class A:
    def abc(self,rad):
        self.rad = rad
        print("Area of circle is:",3.14*self.rad*self.rad)
        
class B(A):
    def abc(self,len,breadth):
        self.len = len
        self.breadth = breadth
        print("Area of rectangle is:",self.len*self.breadth)
        
b = B()
b.abc(5,10)
a = A()
a.abc(5)
