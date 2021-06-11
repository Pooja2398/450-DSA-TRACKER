def kth(arr,k):
    arr.sort()
    return arr[k-1]
if __name__=='__main__':
    import random
    n=int(input())
    arr=list(map(int,input().strip().split()))
    k=int(input())
    print(kth(arr,k))