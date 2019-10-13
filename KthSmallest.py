class find_small:
    def smallest(self,a,k):
        b=a[:k+1]        
        b.sort()
        #print(b)        
        return b[0]
    def largest(self,a,k):
        b=a[:k+1]        
        b.sort()
        #print(b)        
        return b[k]
        
a =[7,8,5,1,4]
f1=find_small()
k=2
b =f1.smallest(a,k)
c =f1.largest(a,k)
print(b,c)
