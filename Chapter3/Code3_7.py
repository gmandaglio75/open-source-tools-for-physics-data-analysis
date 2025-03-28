
class operation:
    first =1
    second = 1
    def __init__(self,a,b):
        self.first= a
        self.second= b
    def changeFS(self,a,b):
        self.first= a
        self.second= b
    def changeF(self,a):
        self.first= a
    def changeS(self,a):
        self.second= a
    def GetF(self):
        return self.first
    def GetS(self):
        return self.second
    def Sum(self):
        return self.first +self.second
    def FminusS(self):
        return self.first -self.second
    def SminusF(self):
        return self.second -self.first
    def Product(self):
        return self.first *self.second
    def SdividebyF(self):
        return self.second /self.first
objvar = operation(2,3)
print(objvar.Sum())
print(objvar.SdividebyF())
objvar.first =20
print(objvar.GetF())
