 def sb(self, a, n, x):
        i=0
        j=0
        ans=n+1
        sum=0
        while(j<n):
            while(sum<=x and j<n):
                sum+=a[j]
                j+=1
            while(sum>x and i<n):
                ans=min(ans,j-i)
                sum-=a[i]
                i+=1
        return ans
