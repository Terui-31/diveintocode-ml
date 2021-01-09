# 【問題1】乱数の作成

import numpy as np

mu = [-3, 0]
sigma = [[1.0, 0.8], [0.8, 1.0]]

# ランダムシード
np.random.seed(0)

# 2次元正規乱数を500個生成
values = np.random.multivariate_normal(mu, sigma, 500)

# 型の確認
print(values.shape)



# 【問題2】散布図による可視化

import matplotlib.pyplot as plt

plt.xlabel("x1")
plt.ylabel("x2")
plt.title("scatter")

# X軸にvaluesの0列目、Y軸に１列目を指定
plt.scatter(values[:,0], values[:,1])
plt.show()



# 【問題3】ヒストグラムによる可視化

plt.title("histogram of x1")
plt.xlabel("x1")
plt.ylabel("frequency")
plt.xlim(-6, 3)
plt.hist(values[:, 0], bins=50)
plt.show()

plt.title("histogram of x2")
plt.xlabel("x2")
plt.ylabel("frequency")
plt.xlim(-6, 3)
plt.hist(values[:, 1], bins=50)
plt.show()



# 【問題4】データの追加

# 新たな2次元正規乱数を500個生成
mu2 = [0, -3]
sigma2 = [[1.0, 0.8], [0.8, 1.0]]
np.random.seed(1)
values2 = np.random.multivariate_normal(mu2, sigma2, 500)

#散布図を重ねる
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("scatter")

plt.scatter(values[:, 0], values[:, 1], label="0")
plt.scatter(values2[:, 0], values2[:, 1], label="1")

plt.legend()
plt.show()



# 【問題5】データの結合

join_values = np.concatenate((values, values2))
print(join_values.shape)



# 【問題6】ラベル付け

# ラベル列作成
new_column1 = np.zeros(500).reshape(500, 1)
new_column2 = np.ones(500).reshape(500, 1)
new_column = np.concatenate((new_column1, new_column2))

# 元データにラベル列を結合
new_join_values = np.concatenate((join_values, new_column), axis=1)
print(new_join_values.shape)

# 確認用
print(new_join_values[499:501])
print(values[499])
print(values2[0])