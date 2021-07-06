def cnk(n,k):
    if k==0:
        return 1
    else:
        if n<k:
            return 0
    return cnk(n-1,k)+cnk(n-1,k-1)

n=10
k=5
res=cnk(n,k)
print (res)
