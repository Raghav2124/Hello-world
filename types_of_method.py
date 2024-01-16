class student:
    school='St John,s High School'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1=value
    @classmethod
    def info(cls):
        return cls.school
s1=student(23,34,45)
s2=student(67,98,21)
print(s1.avg())
print(s2.avg())
print(student.info())#error is shown because we didn'tg paqss cls so 