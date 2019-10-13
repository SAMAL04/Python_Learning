class merge_sort():
    def merge(self,a):        
        if len(a)>1:
            mid =len(a)//2
            L =a[:mid]
            R =a[mid:]
            #if len(L) > 1 and len(R)> 1:    
            m1.merge(L)
            m1.merge(R)
            #print(L)
            #print(R)
            i=j=k=0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    a[k] = L[i]
                    i+=1
                    #print("L")
                    #print(a[k])
                    #k=k+1
                else:
                    a[k] = R[j]
                    j+=1
                    #print("R")
                    #print(a[k])
                k+=1

    def printing(self,a):
        for n in range(len(a)):
            print(a[n])
            
        #print(a)
a =[2,4,3,1,5]
m1=merge_sort()
b= m1.printing(a)
b= m1.merge(a)
b= m1.printing(a)
