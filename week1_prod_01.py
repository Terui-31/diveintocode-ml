# 【問題1】100日目の米粒の数

rices_list = [1]
sum_rices_list = [1]
days = 100

# その日にもらう米の数
for i in range(days-1):
    rices_list.append(rices_list[-1]*2)
    
for i in range(len(rices_list)):
    print("{}日目の米は{}粒".format(i+1 , rices_list[i]))    

# その日までに累計でもらう米の数    
for i in range(days-1):
    sum_rices_list.append(sum_rices_list[-1] + sum_rices_list[-1]*2)    
    
for i in range(len(sum_rices_list)):
    print("{}日目までの米の累計は{}粒".format(i+1 , sum_rices_list[i]))
    
print("100日目には合計で米粒をいくつもらっているのか：{}粒".format(sum_rices_list[-1]))


import matplotlib.pyplot as plt

plt.xlabel("days")
plt.ylabel("mount of rices")
plt.title("mount of rices per days")
plt.plot(rices_list, "ro--", label="per day")
plt.plot(sum_rices_list, "b", label="sum")

plt.legend()
plt.show()



# 【問題2】100日目以外の米粒の数

def compute_sorori_shinzaemon(day=100):
    
    import numpy as np
    
    list_n_grains = [1]
    for i in range(day-1):
        list_n_grains.append(list_n_grains[-1]*2)
        
    list_total_grains = np.sum(list_n_grains)
        
    return print("{}日目の米の数は{}粒で、累計{}粒です。".format(i+2, list_n_grains[i], list_total_grains))
        
compute_sorori_shinzaemon(120)



# 【問題3】貰える米で何人が何日生活できるか

rices = 1329227995784915872903807060280344575
person = 16

def able_survive_days(rices, person):
        
    ''' 
    * 米消費量は一人当たり平均150g/日、約3250粒と仮定
    （参考： https://www.maff.go.jp/j/heya/sodan/1806/03.html ）
    * その３食分を rices_per_person として計算
    '''

    rices_per_person = 3250*3
    
    
    return print("{}粒の米で{}人なら、{}日間生活できる。".format(rices, person, rices // (person * rices_per_person)))

able_survive_days(rices, person)