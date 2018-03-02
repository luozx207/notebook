#-*-coding:utf-8-*-
# 一个数组有 N 个元素，求连续子数组的最大和。
# 例如：[-1,2,1]，和最大的连续子数组为[2,1]，其和为 3
# 输入描述:
# 输入为两行。 第一行一个整数n(1 <= n <= 100000)，表示一共有n个元素
# 第二行为n个数，即每个元素,每个整数都在32位int范围内。以空格分隔。
#
# 输出描述:
# 所有连续子数组中和最大的值。
#
# 输入例子1:
# 3
# -1 2 1
#
# 输出例子1:
# 3


#O(n^2)版本，超时
# n=input()
# a=[]
# b=[]
# a=[int(x) for x in raw_input().split()]
# for i in range(n-1):
#     m=a[i]
#     sum=0
#     for j in range(i+1,n):
#         sum+=a[j]
#         if sum>m:
#             m=sum
#     b.append(m)
# print max(b)

#动态规划：sum[i+1]=max(sum[i]+a[i+1],a[i+1])
#即，sum[i]若是累赘，则a[i+1]作为起点
n=input()
a=[int(x) for x in raw_input().split()]
sum=0
max=a[0]
for i in range(n):
    if sum>=0:
        sum=sum+a[i]
    else:
        sum=a[i]
    if sum>max:
        max=sum
print max
