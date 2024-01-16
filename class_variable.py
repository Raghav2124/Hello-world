class car:
    wheel=4#they are known as static variables/class variables
    def __init__(self):
        self.mil=10
        self.com="BMW"

c1=car()
c2=car()
car.wheel=5
c1.mil=8
print(c1.com,c1.mil,c1.wheel)
print(c2.com,c2.mil,c2.wheel)