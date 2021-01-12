# 【問題1】富士山を超える最小の折る回数

THICKNESS = 0.00008
fold_thickness = [THICKNESS]
mt_fuji = 3776

while True:
    fold_thickness.append(fold_thickness[-1]*2)
    if fold_thickness[-1] > mt_fuji:
        break
        
print("富士山{}mを超えるのに必要な、紙を折る回数：{}回".format(mt_fuji, len(fold_thickness)-1))



# 【問題2】任意の厚さに対応した関数を作成

def folded_thickness(distance, t_0 = 0.00008):
    fold_thickness = [t_0]
    
    while True:
        fold_thickness.append(fold_thickness[-1]*2)
        if fold_thickness[-1] > distance:
            break
        folded_count = len(fold_thickness)
        
    return folded_count


'''
* 最も近い太陽以外の恒星 = プロキシマ・ケンタウリ
* その距離：4.243 光年 ≒ 4.01419e+16 メートル
'''

proxima_centauri = 4.01419e+16
print("最も近い太陽以外の恒星に到達するのに必要な、紙を折る回数：{}回".format(folded_thickness(proxima_centauri)))



# 【問題3】必要な紙の長さ

import math

def fold_paper_length(distance, t_0 = 0.00008):
    fold_thickness = [t_0]
    
    while True:
        fold_thickness.append(fold_thickness[-1]*2)
        if fold_thickness[-1] > distance:
            break
        folded_count = len(fold_thickness)
        
    paper_length = math.pi * t_0 / 6  * (2**folded_count + 4) * (2**folded_count - 1)
        
    return paper_length


# 月
the_moon = 384400000
print("月に届くために必要な紙の長さ：{}m".format(fold_paper_length(the_moon)))

# 富士山
mt_fuji = 3776
print("富士山に届くために必要な紙の長さ：{}m".format(fold_paper_length(mt_fuji)))

# 最も近い太陽以外の恒星
proxima_centauri = 4.01419e+16
print("最も近い太陽以外の恒星に届くために必要な紙の長さ：{}m".format(fold_paper_length(proxima_centauri)))