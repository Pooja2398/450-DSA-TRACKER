def doUnion(self,a,n,b,m):
        result=[]
        for i in range(n):
            result.append(a[i])
        for j in range(m):
            if(b[j] not in result):
                result.append(b[j])
        return (len(set(result)))
      
 def doIntersection(self,a,n,b,m):
  result=[]
  for i in range(n):
    for j in range(m):
      if(a[i]==b[j]):
        result.append(a[i])
  return list(set(result))
  
  
