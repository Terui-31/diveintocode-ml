# 【問題】栗まんじゅうが太陽系を覆う日

def bai_bain(doubled, compare_size, minutes_per_doubled=5):
    doubled_list = [doubled]
    minutes_list = [0]
    
    while True:
        doubled_list.append(doubled_list[-1]*2)
        minutes_list.append(minutes_list[-1]+5)
        
        if doubled_list[-1] > compare_size:
            break
        
    doubled_count = len(doubled_list)-1
    minutes = minutes_list[-1]
        
    return minutes, doubled_count, minutes_list, doubled_list


'''
球の体積の公式：4πr^3 /  3
硬式野球ボールの半径：36 mm
東京ドームの体積：124万 m^3
'''

import math

ball = 4*math.pi*0.036**3 / 3
tokyo_dome = 1240000
minutes_per_doubled=5

minutes, doubled_count, minutes_list, doubled_list = bai_bain(ball, tokyo_dome)
print("{}分後には覆われている(元の{}倍)。".format(minutes, doubled_count))

import matplotlib.pyplot as plt

plt.title("ball covers tokyo_dome")
plt.xlabel("minutes")
plt.ylabel("transition of size")
plt.hlines(tokyo_dome, 0, minutes, "red")
plt.plot(minutes_list, doubled_list, "o--")

plt.show()


'''
球の体積の公式：4πr^3 /  3

栗饅頭の半径：0.025 m

最も遠い太陽系外惑星：MOA-2011-BLG-293Lb
その距離：2万3300光年 ≒ 2.20435e+20 m

参考： https://ja.wikipedia.org/wiki/最も近い・遠い天体の一覧
'''

import math

kuriman = 4*math.pi*0.025**3 / 3
solar_system = 4*math.pi*2.20435e+20**3 / 3
minutes_per_doubled=5

minutes, doubled_count, minutes_list, doubled_list = bai_bain(kuriman, solar_system)
print("{}分後には覆われている(元の{}倍)。".format(minutes, doubled_count))

import matplotlib.pyplot as plt

plt.title("kuriman covers the solar system")
plt.xlabel("minutes")
plt.ylabel("transition of size")
plt.xlim(1000, 1100)
plt.hlines(solar_system, 0, minutes, "red")
plt.plot(minutes_list, doubled_list, "o--")

plt.show()