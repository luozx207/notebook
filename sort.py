#-*-coding:utf-8-*-
import random
import time

def bubble_sort(a):
    n=len(a)
    while n>1:
      for i in range(n-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
      n+=-1
    return a

def insert_sort(a):
    n=len(a)
    for i in range(1,n):
      for j in range(i):
            if a[j]>a[i]:
              temp=a[i]
              del a[i]
              a.insert(j,temp)
              break
      print a

def select_sort(a):
    n=len(a)
    for i in range(n-1):
        minn= a[i]
        j=i
        for j in range(i,n):
            if a[j]<=minn:
                 minn=a[j]
                 k=j
        a[i],a[k]=minn,a[i]
        print a

def quick_sort(a):
    n=len(a)
    if n<2:
        return a
    i=0
    j=n-1
    pivot=a[0]
    while i<j:
        while i<j and a[j]>=pivot:
            j-=1
        a[i],a[j]=a[j],a[i]
        while i<j and a[i]<=pivot:
            i+=1
        a[i],a[j]=a[j],a[i]
    return quick_sort(a[:i])+[pivot]+quick_sort(a[i+1:])

def merge_sort(a):
    result=[]
    n=len(a)
    if n<2:
        return a
    mid=n/2
    b=merge_sort(a[:mid])
    c=merge_sort(a[mid:])
    i=0
    j=0
    while i<mid and j<mid:
        if b[i]>c[j]:
            result.append(c[j])
            j+=1
        else:
            result.append(b[i])
            i+=1
    result=result+b[i:]+c[j:]
    return result


if __name__=='__main__':
    a=[]
    for i in range(20):
        a.append(random.randint(1,20))
    print quick_sort(a)
