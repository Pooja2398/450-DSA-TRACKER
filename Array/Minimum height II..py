def getMinDiff(self, arr, n, k):
        # code here
        for i in range(n):
            if(arr[i]<k):
                arr[i]=arr[i]+k
            else:
                arr[i]=arr[i]-k
            arr.sort()
        minimum=arr[0]
        maximum=arr[len(arr)-1]
        return(maximum-minimum)
