a=[1, 4, 5, 9, 1]
n=len(a)
ans=0
i,j=0,n-1
while(i<=j):
    if(a[i]==a[j]):
        i+=1 
        j-=1 
    elif(a[i]<a[j]):
        i+=1 
        a[i]+=a[i-1]
        ans+=1 
    else:
        j-=1 
        a[j]+=a[j+1]
        ans+=1 
print(ans)
