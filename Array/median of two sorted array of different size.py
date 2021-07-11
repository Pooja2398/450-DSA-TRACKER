def getMedian(ar1, ar2, n, m) :
  ar1[n:]=ar2
  ar1.sort()
  k=len(ar1)
  if(k%2==0):
     median=(ar1[k//2]+ar1[(k//2)+1])/2
  else:
     median=ar1[k//2]
  return(median)
