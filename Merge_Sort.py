class merge_sort():
    def split_func(self,a):
        splitted_list = a        
        b=len(splitted_list)        
        n=0
        #for x in splitted_list:
        n=n+2
            
            #print(x)
        split_half = int(b/2)        
        splitted_list.append(a[0:split_half])
        splitted_list.append(a[split_half:b])
        
        #splitted_list.remove(splitted_list[0])
        #print(len(splitted_list))
        return splitted_list
a= [3,56,17,4,8,10,99]
m1=merge_sort()
s = m1.split_func(a)
print(s)
