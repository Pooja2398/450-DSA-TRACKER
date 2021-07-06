def maxSubArraySum(self,a,size):
        ##Your code here
        if(size==1):
            return a[0]
        max_so_far=a[0]
        curr=a[0]
        for i in range(1,size):
            curr=max(a[i],curr+a[i])
            max_so_far=max(curr,max_so_far)
        return max_so_far
