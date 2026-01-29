


class d:
    def __init__(self):
        self.a=int(input())
        self.arr=[5,2,10]
    def display(self):
        if self.a==1:
            print(self.arr[0]+self.arr[2])
        elif self.a==2:
            print(self.arr[2]-self.arr[1])
        elif self.a==3:
            print(self.arr[1]*self.arr[0])
        elif self.a==4:
            print(self.arr[0]/self.arr[1])

h1=d()
h1.display()
            
            
