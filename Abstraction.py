#Hiding Internal Process
class calculator:
    def add(self,x,y):
        return x+y
    def subtract(self,x,y):
        return x-y
x = 10
y = 20
obj = calculator()
add = obj.add(x,y)
print(add)