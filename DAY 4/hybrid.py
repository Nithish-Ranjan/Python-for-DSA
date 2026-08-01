class A:
    def dispA(self):
        print("Constructor of class A")
        
class B(A):
    def dispB(self):
        super().dispA()
        print("Constructor of class B")
  
class C:
    def dispC(self):
        print("Constructor of class C")
   
class D(B, C):
    def dispD(self):
        super().dispB()
        super().dispC()
        print("Constructor of class D")
   
d =D()
d.dispD()