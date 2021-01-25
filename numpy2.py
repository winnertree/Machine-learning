import numpy as np

# A = np.array([[1,2,3],[4,5,6]])
# B = np.array([[-1,-2],[-3,-4],[-5,-6]])
#
# C = np.dot(A,B) # 행렬 곱 수행
#
# print("A.shape == {} , B.shape == {}".format(A.shape,B.shape))
# print("C.shape == {}".format(C.shape))
# print(C)

# 브로드캐스트 : 차원이 작은 쪽이 큰 쪽의 행 단위로 반복적으로 크기를 맞춘 후 계산, 곱셈은 안됨
# A = np.array([[1,2],[3,4]])
# b = 5
# print(A+b) # b를 [[5,5],[5,5]]로 바꿔주는 브로드캐스트를 통해 계산

# 전치행렬(transpose) : 원본 행렬의 열은 행으로, 행은 열로 바꾼 행렬
# A = np.array([[1,2],[3,4],[5,6]])
# B = A.T
# print("A.shape == {}, B.shape == {}".format(A.shape, B.shape))
# print(A,"\n",B)
#
# C = np.array([1,2,3,4,5])
# D = C.T     # C는 백터 이므로 transpose 안됨
# E = C.reshape(1,5)  # 1*5 matrix
# F = E.T     # E의 전치행렬
# print("C.shape == {}, D.shape == {}".format(C.shape, D.shape))
# print("E.shape == {}, F.shape == {}".format(E.shape, F.shape))
# print(F)

# 행렬 indexing / slicing
# A = np.array([10,20,30,40,50,60]).reshape(3,2)
# print("A.shape == {}".format(A.shape))
# print(A)
# print("A[0,0] == {}, A[2,1] == {}".format(A[0,0],A[2,1]))
#
# print("A[0:-1 , 1:2] == {}".format(A[0:-1, 1:2])) # 0~-2행까지 1부터 1열까지
# print("A[:,0] == {}".format(A[:,0])) # 모든 행의 0열
# print("A[: ,:] == {}".format(A[:,:]))   # 모든 행, 모든 열

# iterator : 행렬 모든 원소를 access 하는 경우에 사용
A = np.array([[10,20,30,40],[50,60,70,80]])
print(A)
print("A.shape == {}".format(A.shape))

it = np.nditer(A, flags=['multi_index'], op_flags=['readwrite'])

while not it.finished:
    idx = it.multi_index
    print("Current value => {}".format(A[idx]))
    it.iternext()