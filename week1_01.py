#問題１
"""
紙を1回折った時の厚さを計算するコード
"""
THICKNESS = 0.00008
folded_thickness = THICKNESS*(2**43)
print("厚さ： {}メートル".format(folded_thickness))



#問題2
print("厚さ： {:.2f}万キロメートル".format(folded_thickness/10000000))



#問題3
init1 = 2
for i in range(42):
    init1 *= 2
folded_thickness1 = init1 * THICKNESS
print("厚さ： {:.2f}万キロメートル".format(folded_thickness1/10000000))



#問題4
#べき乗
%%timeit
import time
start = time.time()
#####
folded_thickness = THICKNESS*(2**43)
#####
elapsed_time = time.time() - start
print("time : {}[s]".format(elapsed_time))

%%timeit
#for文
import time
start = time.time()
init2 = 2
#####
for i in range(42):
    init2 *= 2
folded_thickness2 = init2 * THICKNESS
#####
elapsed_time = time.time() - start
print("time : {}[s]".format(elapsed_time))

#べき乗の方が、for文より計算が早い



#問題5
init3 = 2
fold_list = []
fold_list.append(THICKNESS)
fold_list.append(init3)
for i in range(42):
    init3 *= 2
    fold_list.append(init3)
folded_thickness1 = init3 * THICKNESS
print(len(fold_list))



#問題6
"""
グラフを表示する。タイトルと軸ラベル名付き。
"""
import matplotlib.pyplot as plt
%matplotlib inline
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.plot(fold_list) # 「リスト名」のところにリストの変数名を入れる
plt.show()
print(fold_list)

#カスタム１
import matplotlib.pyplot as plt
%matplotlib inline
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.plot(fold_list, color = 'red')
plt.show()

#カスタム２
import matplotlib.pyplot as plt
%matplotlib inline
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.plot(fold_list, '--r', color = 'red', marker='o')
plt.show()

#カスタム3
import matplotlib.pyplot as plt
%matplotlib inline

plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.xlim(0, 10)
plt.ylim(0, 1000)
plt.plot(fold_list, '--r', color = 'red', marker='o')

plt.subplot(2, 2, 2)
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.xlim(10, 20)
plt.ylim(0, 1200000)
plt.plot(fold_list, '--r', color = 'red', marker='o')

plt.subplot(2, 2, 3)
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.xlim(20, 30)
plt.ylim(0, 1200000000)
plt.plot(fold_list, '--r', color = 'red', marker='o')

plt.subplot(2, 2, 4)
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.xlim(30, 43)
plt.plot(fold_list, '--r', color = 'red', marker='o')

plt.show()