
import json
import time


with open('damage.json', encoding='utf-8') as f:
    b = json.load(f)

c = b['challenges']
strattime = 1598227476
recodes = []
for i in c:
    #print(i)
    time_ = i['challenge_time']
    if time_ >= strattime:
        recodes.append(i)

name = b['members']
trans = {}
for i in name:
    trans[i['qqid']] = i['nickname']

qq = {}
total_damage = [[0] * 5 for i in range(2)]
max_damage = [[0] * 5 for i in range(2)]
dao_num = [[0] * 5 for i in range(2)]
qq_id_max = [[0] * 5 for i in range(2)]
for i in recodes:
  
    #print(i)
    qq_id = i['qqid']
    boss_id = i['boss_num'] - 1
    damage = i['damage']
    cycle = i['cycle'] - 1
    #print(boss_id,damage,cycle)
    health_ramain = i['health_ramain']
    is_continue = i['is_continue']
    if not is_continue:
        if qq_id in qq:
            qq[qq_id] += 1
        else:
            qq[qq_id] = 1
    if health_ramain != 0 and not is_continue:
        if cycle == 0:
            max_damage[0][boss_id] = max(damage,max_damage[0][boss_id])
            total_damage[0][boss_id] += damage
            if damage != 0:
                dao_num[0][boss_id] += 1
            if damage == max_damage[0][boss_id]:
                qq_id_max[0][boss_id] = qq_id
        else:
            max_damage[1][boss_id] = max(damage,max_damage[1][boss_id])
            total_damage[1][boss_id] += damage
            if damage != 0:
                dao_num[1][boss_id] += 1
            if damage == max_damage[1][boss_id]:
                qq_id_max[1][boss_id] = qq_id

print(qq)
avg = [[0] * 5 for i in range(2)]
for i in range(2):
    for j in range(5):
        avg[i][j] = total_damage[i][j] / dao_num[i][j]

print(max_damage)

qq_equal = {}

#cal = max_damage
cal = avg
print(cal)
for i in recodes:
  
    #print(i)
    qq_id = i['qqid']
    boss_id = i['boss_num'] - 1
    damage = i['damage']
    cycle = i['cycle'] - 1
    if qq_id not in qq_equal:
        qq_equal[qq_id] = [0] * 5
    if cycle == 0:
        qq_equal[qq_id][boss_id] += damage / cal[0][boss_id]
    else:
        qq_equal[qq_id][boss_id] += damage / cal[1][boss_id]

vec = []
for k,v in qq_equal.items():
    vec.append((k,sum(v)))

vec.sort(key= lambda x:-x[1])


#for i in qq_id_max[0]:
#    print("一阶段最高伤害：",trans[i])


for index,i in enumerate(qq_id_max[1]):
    print(str(index + 1) + "王最高伤害：",max_damage[1][index],'出刀者：',trans[i])

print('等效刀数：')
for index,i in enumerate(vec):
    #if index < 5:
    if index < 30:
        print(trans[i[0]],str(i[1])[:5])
    #print(index+1,str(i[1])[:6])



name = [trans[i[0]] for i in vec]
name_ = [trans[i[0]][:3] for i in vec]
s = [i[1] for i in vec]

#import matplotlib.pyplot as plt
#plt.bar(name_,s)
#plt.rcParams['font.sans-serif'] = ['SimHei']
#plt.show()


#import random
#随机抽一个前5送上神秘奖励
#print(random.choice(name[0:5]))
