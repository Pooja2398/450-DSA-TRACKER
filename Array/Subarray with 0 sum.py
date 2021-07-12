def subArrayExists(self,arr,n):
    sum=0
    ans="Yes"
    s=set()
    for i in range(n):
        sum+=arr[i]
        if(sum==0 or sum in s):
            return True
        s.add(sum)
