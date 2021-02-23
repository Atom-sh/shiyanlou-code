#jump7.py

# for循环遍历集合1~100赋给i。 Loop through a collection
for i in range(1,101):
    str = '{}'.format(i) #将i转化为字符串。
    if i % 7 == 0 or '7' in str: # 如果 i 是 7 的倍数 或 i 是含 7 的数字。
        continue #跳过本轮循环，不打印i
    else:
        print('{}'.format(i)) #打印i
