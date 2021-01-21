# import numpy as np
# arr = np.array([1, 2, 3])
# print(arr.size) # 배열의 크기
# print(arr.dtype) # 배열 원소의 타입
# print(arr[2]) # 인덱스 2의 원소

# from numpy import exp
# result=exp(1)
# print("result == ", result, ",type == ", type(result))

# from numpy import *
# result = exp(1) + log10(7) + sqrt(2)
# print(result)

# import numpy as np
# A = np.array([[1,0],[0,1]])
# B = np.array([[1,1],[1,1]])
# print(A+B) #행렬 연산

#벡터
# import numpy as np
# A = np.array([1,2,3])
# B = np.array([4,5,6])
# print(A , B)
# print("A.shape == {}, B.shape == {}".format(A.shape,B.shape)) # 형상 출력
# print("A.ndim == {}, B.ndim == {}".format(A.ndim,B.ndim)) # 차원 출력
# print("A + B == {}, A - B == {}, A*B == {}, A / B == {}".format(A+B,A-B,A*B,A/B))

# 이차원 행렬
import numpy as np
A = np.array([[1, 2, 3],[4, 5, 6]])
B = np.array([[-1, -2, -3],[-4, -5, -6]])
print("A.shape == {}, B.shape == {}".format(A.shape,B.shape)) # 형상 출력
print("A.ndim == {}, B.ndim == {}".format(A.ndim,B.ndim)) # 차원 출력

#형 변환
C = np.array([1,2,3])
print("C.shape == {}".format(C.shape))

C = C.reshape(1,3) # 형 변환
print("C.shape == {}".format(C.shape))