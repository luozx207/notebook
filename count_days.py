output=[]
m=[31,28,31,30,31,30,31,31,30,31,30,31]
while 1:
    a=[int(x) for x in raw_input().split()]
    if not a:
        break
    result=0
    if a[0]%4==0:
        if a[1]>2:
            result+=1
    for i in range(a[1]-1):
        result+=m[i]
    result+=a[2]
    output.append(result)
for o in output:
    print o
