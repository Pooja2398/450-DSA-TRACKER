a=[-2,4,-9,63,-256,0]
j=0
for i in range(len(a)):
    if(a[i]<0):
        temp=a[i]
        a[i]=a[j]
        a[j]=temp
        j=j+1 
print(a)
