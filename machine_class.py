# class PrivateMemberTest:
#     def __init__(self, name1, name2):
#         self.name1=name1
#         self.__name2=name2 # private 변수
#         print("Initialized with" + name1 + "," +name2)
#
#     def getNames(self):
#         self.__printNames()
#         return self.name1,self.__name2
#
#     def __printNames(self): # private method
#         print(self.name1,self.__name2)
#
# obj=PrivateMemberTest("Kim", "Lee")
#
# print(obj.name1)
# print(obj.getNames())
# print(obj.__printNames()) # error, private method 이므로 접근 안됨
# print(obj.__name2) # error, private variable 이므로 접근 안됨

##########

def print_name(name):
    print("[def] ", name)

class SameTest:
    def __init__(self):
        pass

    def print_name(self,name): # 외부 함수와 동일한 이름으로 method 정의
        print("[SameTest] ", name)

    def call_test(self):
        print_name("Kim") # 외부 함수 호출
        self.print_name("Kim") # 클래스 내부 method 호출

obj = SameTest()

print_name("Park")

obj.print_name("Lee")

obj.call_test()