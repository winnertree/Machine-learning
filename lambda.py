# lambda 함수
# 함수명 = lambda 입력1, 입력2,...: 대체되는 표현식

# f = lambda x : x+100  # f(x) = x + 100
# for i in range(3):
#     print(f(i))

# def print_hello():
#     print("hello python")
#
# def test_lambda(s,t):
#     print("input 1 == {}, input 2 =={}".format(s,t))
#
# s=100
# t=200
#
# fx=lambda x,y : test_lambda(s,t)
# fy=lambda x,y : print_hello()
#
# fx(500,1000)
# fy(300,600)

#class
class Person:

    cnt = 0

    def __init__(self, name):
        self.name=name
        Person.cnt+=1
        print("{} is initialized".format(self.name))

    def work(self,company):
        print("{} is working in {}".format(self.name,company))

    def sleep(self):
        print("{} is sleeping".format(self.name))

    @classmethod
    def getCount(cls): #class method
        return cls.cnt

obj=Person("Park")

obj.work("AAAA")
obj.sleep()

print(obj.name)

print(Person.getCount())
print(Person.cnt)