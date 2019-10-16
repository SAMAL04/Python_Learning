class Employee():
    def __init__(self,a):
        self.empid = a[0]
        self.value = a[1]
        self.subord =a[2]


a = [1,15,2]
e = Employee(a)
print(e)
