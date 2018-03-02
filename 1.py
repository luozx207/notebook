import bisect
def binarysearch(v,a,n):
    left,right=0,n-1
    while left<=right:
        mid=(left+right)/2
        if v>a[mid]:
            left=mid+1
        elif v<a[mid]:
            right=mid-1
        else:
            return mid

def binarysearch_left(v,a,n):
    if v>a[n-1]:
        return n
    if v<a[0]:
        return 0
    left,right=0,n-1
    while left+1<right:
        mid=(left+right)/2
        if v>a[mid]:
            left=mid
        else:
            right=mid
    return right
if __name__=="__main__":
    a=[1,2,3,4,5,6,7]
    index=bisect.bisect_left(a,6.5)
    print binarysearch_left(2.3,a,7)
    print a
