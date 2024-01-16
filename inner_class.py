class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.rollno)
        class laptop:
            def __init__(self):
                self.brand='Hp'
                self.cpu='i5'
                self.ram=8

s1=student('Raghav',20)
s2=student('Tushar',20)
s1.show()