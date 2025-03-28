class shape:
    base =1
    height = 1
    def __init__(self,a,b):
        self.base= a
        self.height= b
    def changeBH(self,a,b):
        self.base= a
        self.height= b
    def changeB(self,a):
        self.base= a
    def changeH(self,a):
        self.height= a
    def GetB(self):
        return self.base
    def GetH(self):
        return self.height
class rectangle(shape):
    def area(self):
        return self.base *self.height
class triange(shape):
    def area(self):
        return self.base *self.height/2
￼
objvar = rectangle(2,3)
print("showing the use of the mather class GetB", objvar.GetB())
print(objvar.area())
objvar = triange(2,3)
print("showing the use of the mather class GetH", objvar.GetH())
print(objvar.area())
