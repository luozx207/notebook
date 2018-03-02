#-*-coding:utf-8-*-
# 某餐馆有n张桌子，每张桌子有一个参数：a 可容纳的最大人数;
# 有m批客人，每批客人有两个参数:b人数，c预计消费金额。
# 在不允许拼桌的情况下，请实现一个算法选择其中一部分客人，使得总预计消费金额最大
#
# 输入描述:
# 输入包括m+2行。 第一行两个整数n(1 <= n <= 50000),m(1 <= m <= 50000)
# 第二行为n个参数a,即每个桌子可容纳的最大人数,以空格分隔,范围均在32位int范围内。
# 接下来m行，每行两个参数b,c。分别表示第i批客人的人数和预计消费金额,以空格分隔,范围均在32位int范围内。
#
#
# 输出描述:
# 输出一个整数,表示最大的总预计消费金额
#
# 输入例子1:
# 3 5
# 2 4 2
# 1 3
# 3 5
# 3 7
# 5 9
# 1 10
#
# 输出例子1:
# 20
import bisect
n,m=[int(x) for x in raw_input().split()]
a=[int(x) for x in raw_input().split()]
a.sort()
customer=[]
for i in range(m):
    customer.append([int (x) for x in raw_input().split()])
# 不需要用字典
customer =sorted(customer ,key=lambda x:x[1],reverse=True)
#就差最后一步了，将customer一个个插入a,找到合适的位置，并删除那个位置的元素
sum=0
for c in customer:
    n=len(a)
#     while i<n and a[i]<c[0]:
#         i+=1
# 超时，改用二分查找
    index=bisect.bisect_left(a,c[0])
    print a
#bisect:二分查找库
    if index<n:
        sum+=c[1]
        del a[index]
    if len(a)==0:
        break
print sum
