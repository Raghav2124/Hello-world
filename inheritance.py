#parent class /super class
class a:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

#child class/sub class
class b(a):#way to define child class
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")
a1=a()
a1.feature1()
a1.feature2()
b1=b()
b1.feature1()