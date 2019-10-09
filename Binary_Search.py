class bin_search():
    
    def mid(self,high,low,inp,a):
        
        while low != high:
            a=a[low:high] 
            print(a)
            mid_val = int((high-low)/2)
            print(mid_val)
            if a[mid_val] > inp:
                print(a[mid_val])
                high = mid_val
                low=0
                print("HIGH")
                #print(high)
            elif a[mid_val] < inp:
                low = mid_val
                high =len(a)
                print("LOW")
                print(low)
        
            if a[mid_val] == inp:
                print("Value available")
                break
            #else:
                #print("Not Available")
                
         
        
a = [1,2,3,4,5,6,7,8,9]
low = 0
high = len(a)
inp  = 5
b1=bin_search()
b1.mid(high,low,inp,a)
