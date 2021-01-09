# 【問題1】2×2マスのチェス盤の小麦の数

n_squares = 4
small_board_list = [1]
for i in range(n_squares - 1):
    small_board_list.append(2*small_board_list[-1])

import numpy as np
small_board_ndarray = np.array(small_board_list)

# ndarrayの変形(１行４列→２行２列)
small_board_ndarray2 = small_board_ndarray.reshape(2, 2)
print(small_board_ndarray2)



# 【問題2】n×mマスへの拡張

# nm_chessboardは第１引数に行数、第２引数に列数をとり、各マスの小麦の数を返す

'''
n_array：小麦を載せるボードを１行に伸ばしているもの（標準Pythonのarray形式）
nm_board_list：n_arrayに載せる小麦の数のリスト
n_ndarray：小麦が載っているボードを１行に伸ばしているもの（Numpyのarray形式）
nm_ndarray：n_ndarrayをn×m行列化したもの
'''

def nm_chessboard(n, m):
    import numpy as np
    n_array = n*m
    nm_board_list = [1]
    for i in range(n_array - 1):
        nm_board_list.append(2*nm_board_list[-1])
    n_ndarray = np.array(nm_board_list)
    nm_ndarray = n_ndarray.reshape(n, m)
    return nm_ndarray

# 8×8マスのチェス盤の小麦の数を出力
print(nm_chessboard(8, 8))



# 【問題3】小麦の数の合計

# numpy.sum()でNumpy配列全体の合計値を出力
print(np.sum(nm_chessboard(8, 8)))

# 棒グラフ化
import matplotlib.pyplot as plt
%matplotlib inline
plt.xlabel("column")
plt.ylabel("number of wheat")
plt.title("number of wheat in each column")

# X軸用の等差数列を生成
left = np.arange(1, 9)

#Y軸に小麦の数の平均値を入れる（axis=0で列指定）
height = np.mean(nm_chessboard(8, 8), axis=0)
plt.bar(left, height)
plt.show()



# 【問題4】小麦の数のヒートマップ

plt.xlabel("column")
plt.ylabel("row")
plt.title("heatmap")
plt.pcolor(nm_chessboard(8, 8))
plt.show()



# 【問題5】後半は前半の何倍か

# チェス盤を8×8とすると、
chess_regular = nm_chessboard(8, 8)

# 前半（０〜３行目）
chess_regular_prev = chess_regular[0:4]

# 後半（４〜７行目）
chess_regular_next = chess_regular[4:8]

# 後半の総和 / 前半の総和
print(np.sum(chess_regular_next) / np.sum(chess_regular_prev))



# 【問題6】他の計算方法によるn×mマスへの拡張

# append()版
def nm_chessboard2(n, m):
    import numpy as np
    n_array = n*m
    nm_board_ndarray = ([1])
    for i in range(n_array - 1):
        nm_board_ndarray = np.append(nm_board_ndarray, 2*nm_board_ndarray[-1]).astype(np.uint64)
    nm_ndarray = nm_board_ndarray.reshape(n, m)
    return nm_ndarray

print(np.sum(nm_chessboard2(8, 8)))


# ブロードキャスト版
def nm_chessboard_broadcast(n, m):
    import numpy as np
    n_array = n*m
    indices_of_squares = np.arange(n_array).astype(np.uint64)
    n_ndarray = 2**indices_of_squares
    nm_ndarray = n_ndarray.reshape(n, m)
    return nm_ndarray

print(np.sum(nm_chessboard_broadcast(8, 8)))



# 【問題7】計算時間の比較

%%timeit
#for文
def nm_chessboard(n, m):
    import numpy as np
    n_array = n*m
    nm_board_list = [1]
    for i in range(n_array - 1):
        nm_board_list.append(2*nm_board_list[-1])
    n_ndarray = np.array(nm_board_list)
    nm_ndarray = n_ndarray.reshape(n, m)
    return nm_ndarray

%%timeit
#append()
def nm_chessboard2(n, m):
    import numpy as np
    n_array = n*m
    nm_board_ndarray = ([1])
    for i in range(n_array - 1):
        nm_board_ndarray = np.append(nm_board_ndarray, 2*nm_board_ndarray[-1]).astype(np.uint64)
    nm_ndarray = nm_board_ndarray.reshape(n, m)
    return nm_ndarray

%%timeit
# ブロードキャスト版
def nm_chessboard_broadcast(n, m):
    import numpy as np
    n_array = n*m
    indices_of_squares = np.arange(n_array).astype(np.uint64)
    n_ndarray = 2**indices_of_squares
    nm_ndarray = n_ndarray.reshape(n, m)
    return nm_ndarray

'''
考察：
実行結果はほぼ同程度だが、何度か試行したところ
* 実行時間の速さ：for文＜append()＜ブロードキャスト
* 標準偏差の小ささ：for文＜append()＜ブロードキャスト
と見て取れた。 
'''