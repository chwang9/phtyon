# 1.输入
# password = input('请输入密码：')
# print('您输入的密码是:',password)

# 2.判断类型
# a = input('输入：')
# print(type(a))
# print('输入了一个数字：%s'%a)

# 3.强制类型转换
# a = int('123')
# print(type(a))
# b = a + 100
# print(b)

# 4.条件判断语句
# if True:
#     print('true')
# else:
#     print('false')
# print('end')

# score = 77
# if score >= 90 and score <=100:
#     print('A')
# elif score >= 80 and score <90:
#     print('B')
# else:
#     print('C')

# 5.引入随机数
# import random
# x = random.randint(0,2) #随机生成随机数0至2
# print(x)

# 6.循环语句
# for i in range(5):
#     print(i)

# 从0开始到13结束，步进值3
# for i in range(0,13,3):
#     print(i)

# name = 'chengdu'
# for x in name:
#     print(x, end='\t')

# a = ['aa', 'bb', 'cc']
# for i in range(len(a)):
#     print(i, a[i])

i = 0
while i < 5:
    print('当前是第%d次'%(i+1))
    print('i=%d'%i)
    i +=1