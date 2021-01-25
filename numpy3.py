import numpy as np

# # concatenate : 행렬에 행 또는 열을 추가하기 위한 함수
# A = np.array([[10,20,30],[40,50,60]])
#
# print(A.shape)
#
# row_add = np.array([70,80,90]).reshape(1,3) # 1행 3열로 reshape, 백터는 행렬이 아니기 때문\
#
# column_add = np.array([1000,2000]).reshape(2,1)
#
# # axis = 0 은 행을 늘릴때
# B = np.concatenate((A, row_add), axis=0)
# print(B)
#
# # axis = 1은 열을 늘릴때
# C = np.concatenate((A, column_add), axis=1)
# print(C)

# 여러가지 함수
# load_data = np.loadtxt('./data-01.csv', delimiter = ',', dtype=np.float32)
# x_data = load_data[:,0:-1]
# t_data = load_data[:,[-1]]

# random_n1 = np.random.rand(3)   # 0과 1 사이의 임의의 실수값을 리턴해주는 함수
# random_n2 = np.random.rand(1,3)
# random_n3 = np.random.rand(3,1)
# print("random_n1 == {}, shape == {}".format(random_n1,random_n1.shape))
# print("random_n2 == {}, shape == {}".format(random_n2,random_n2.shape))
# print("random_n3 == {}, shape == {}".format(random_n3,random_n3.shape))
#
# x = np.array([2,4,6,8])
# print("sum == {}".format(np.sum(x)))
# print("exp == {}".format(np.exp(x)))
# print("log == {}".format(np.log(x)))    # 각각의 원소들을 다 계산해줌

# x = np.array([2,4,6,8])
# print("np.max(x) == {}".format(np.max(x)))
# print("np.min(x) == {}".format(np.min(x)))
# print("np.argmax(x) == {}".format(np.argmax(x))) # 최댓값이 있는 곳의 인댁스
# print("np.argmin(x) == {}".format(np.argmin(x))) # 최솟값이 있는 곳의 인덱스

# x = np.array([[2,4,6],[1,2,3],[0,5,8]])
# print("np.max(x) == {}".format(np.max(x, axis=0))) # 열기준
# print("np.min(x) == {}".format(np.min(x, axis=0)))
#
# print("np.max(x) == {}".format(np.max(x, axis=1))) # 행기준
# print("np.min(x) == {}".format(np.min(x, axis=1)))
#
# print("np.argmax(x) == {}".format(np.argmax(x, axis=0))) # 최댓값이 있는 곳의 인댁스
# print("np.argmin(x) == {}".format(np.argmin(x, axis=1))) # 최솟값이 있는 곳의 인덱스

# A = np.ones([3,3])
# print(A.shape,"\n" ,A)
# B = np.zeros([2,3])
# print(B.shape,"\n" ,B)


# matplotlib, scatter plot
import matplotlib.pyplot as pit
# x_data = np.random.random(100)
# y_data = np.random.random(100)
#
# pit.title('scatter plot')
# pit.grid()
# pit.scatter(x_data,y_data,color='b',marker='o')
# pit.show()

# x_data=[x for x in range(-5,5)]
# y_data=[y*y for y in range(-5,5)]
#
# pit.title('line plot')
# pit.grid()
# pit.plot(x_data,y_data,color='b')
# pit.show()

x_data=[-3,-2,-1,0,1,2,3,4,5,6,7,8,9]
y_data=[-8,-13,-0,3,6,-1,-5,-7,1,8,7,12,13]
pit.title('line plot')
pit.grid()
pit.plot(x_data,y_data,color='b')
pit.show()