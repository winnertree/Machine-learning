#exception

# def calc(list_data):
#     sum=0
#
#     try:
#         sum=list_data[0] + list_data[1] + list_data[2]
#
#         if sum<0:
#             raise Exception("Sum is minus") # 인위적으로 exception 발생 시킴
#
#     except IndexError as err:
#         print(str(err))
#     except Exception as err:
#         print(str(err))
#     finally:
#         print(sum)
#
# calc([1,2,-100])

#with
f = open("./file_test",'w')
f.write("Hello Python!!!")
f.close()

with open("./file_test", 'w') as f:
    f.write("Hello Python!!!")