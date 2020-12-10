#列表(列表可以存储混合类型)
# nameList = ['xiaozhang', 'xiaowang', 'xiaoli']
# print(nameList[0])

# testList = ['xiaozhang', 0]
# print(type(testList[1]))

# nameList = ['xiaozhang', 'xiaowang', 'xiaoli']
# for name in nameList:
#     print(name)

# 增
# nameList = ['xiaozhang', 'xiaowang', 'xiaoli']
# nameList.append(2)
# print(nameList)

# a = [1,2]
# b = [3,4]
# a.append(b)
# print(a)
# a.extend(b)
# print(a)
# a = [0,1,2]
# a.insert(1,3)  # 第一个元素是下标，第二个元素是插入元素
# print(a)

#删
# mouvie = ['HHH', 'www', 'wewewe']
# del mouvie[1] # 删除指定位置的一个元素
# mouvie.pop() # 删除最后一个
# mouvie.remove('HHH') # 移除直接删除指定内容的元素
# print(mouvie)

#改
# mouvie = ['HHH', 'www', 'wewewe']
# mouvie[2] = '333'
# print(mouvie)

# 查
# mouvie = ['HHH', 'www', 'wewewe']
# findName = input("姓名")
# if findName in mouvie:
#     print('找到')
# else:
#     print('wu')

# a = ['a', 'b', 'c', 'a','d']
# print(a.index('a', 1, 4)) # 查找到指定下标范围的元素，并找到对应数据的下标（范围左边闭右开[1,3)）
# print(a.count('a')) # 计数


# 排序与翻转
# a = [1,3,2,5]
# a.reverse() # 翻转
# print(a)
# a.sort() # 正序
# a.sort(reverse=True) # 倒序
# print(a)

# 嵌套
# school = [['北京大学','清华大学'],['南京大学','天津大学'],['山东大学']]
# print(school[0][0])
import random
offices = [[],[],[]]
names = ['A', 'B', 'C','D','E','F','G','H']

for name in names:
    index = random.randint(0,2)
    offices[index].append(name)
i = 1
for office in offices:
    print(i,len(office))
    i+=1
    for name in office:
        print(name, end='\t')
    print('\n')
    print('----------')
    