# 补货异常
# try:
#     print(num)
# except Exception as result:
#     print(result)

try:
    f = open('123.txt', 'r')
except Exception as result:
    print('11111111111')
finally:
    f.close()
    print('guan')

