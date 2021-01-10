# 【問題1】行列積を手計算する

$$
\begin{align}
    \boldsymbol{A} \boldsymbol{B}
    &= 
    \begin{pmatrix}
        -1 & 2  & 3 \\
        4  & -5 & 6 \\
        7  & 8  & -9
    \end{pmatrix}
    \begin{pmatrix}
        0 & 2 & 1  \\
        0 & 2 & -8 \\
        2 & 9 & -1
    \end{pmatrix} \\
    &=
    \begin{pmatrix}
        0+0+6   & -2+4+27   & -1-16-3 \\
        0+0+12 & 8-10+54   & 4+40-6 \\
        0+0-18  & 14+16-81 & 7-64+9
    \end{pmatrix} \\
    &=
    \begin{pmatrix}
        6    & 29  & -20 \\
        12  & 52  &  38 \\
        -18 & -51 & -48
    \end{pmatrix}
\end{align}
$$



# 【問題2】NumPyの関数による計算

import numpy as np
a_ndarray = np.array([[-1, 2, 3], [4, -5, 6], [7, 8, -9]])
b_ndarray = np.array([[0, 2, 1], [0, 2, -8], [2, 9, -1]])

# dot
c_ndarray_dot = np.dot(a_ndarray, b_ndarray)
print(c_ndarray_dot)

# matmul
c_ndarray_matmul = np.matmul(a_ndarray, b_ndarray)
print(c_ndarray_matmul)

# @
c_ndarray_at = a_ndarray @ b_ndarray
print(c_ndarray_at)



# 【問題3】ある要素の計算を実装

c_ndarray_00_00 = a_ndarray[0, 0] * b_ndarray[0, 0]
c_ndarray_00_10 = a_ndarray[0, 0] * b_ndarray[1, 0]
c_ndarray_00_20 = a_ndarray[0, 0] * b_ndarray[2, 0]
c_ndarray_0_0 = np.sum((c_ndarray_00_00, c_ndarray_00_10, c_ndarray_00_20))
print(c_ndarray_0_0)



# 【問題4】行列積を行う関数の作成

def dot_ndarray(a, b):

    import numpy as np
    
    c = np.zeros((a.shape[0], b.shape[1]))
    ii = c.shape[0]
    jj = c.shape[1]
    kk = a.shape[0]
    
    for i in range(ii):
        for j in range(jj):
            for k in range(kk):
                c[i][j] += a[i][k] * b[k][j]
    return(c)

print(dot_ndarray(a_ndarray, b_ndarray))



# 【問題5】計算が定義されない入力を判定する

d_ndarray = np.array([[-1, 2, 3], [4, -5, 6]])
e_ndarray = np.array([[-9, 8, 7], [6, -5, 4]])

def dot_ndarray2(a, b):

    import numpy as np
    
    c = np.zeros((a.shape[0], b.shape[1]))
    ii = c.shape[0]
    jj = c.shape[1]
    kk = a.shape[0]
    
    if a.shape[1] == b.shape[0]:
        
        for i in range(ii):
            for j in range(jj):
                for k in range(kk):
                    c[i][j] += a[i][k] * b[k][j]
        return(c)
    
    else:
        
        print("行列積の演算における各行列の型が一致しません。")
        return("---type_incorrect_error---")
        
print(dot_ndarray2(d_ndarray, e_ndarray))



# 【問題6】転置

e_ndarray_t = e_ndarray.T
print(dot_ndarray2(d_ndarray, e_ndarray_t))