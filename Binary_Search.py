import math
class bin_search:
    
    def get_inp(self,a): 
        #print(a)
        l = len(a)
        div_two = l/2
        ty_pe = type(div_two)
        list_in =[div_two,ty_pe]
        #print(list_in)
        return list_in

    def find_centre(self,inp):
        #print(inp)
        cen = inp[0]
        if inp[1] ==  float:
            centre_element =math.ceil(cen)
            
        else:
            centre_element =cen
            
        return centre_element
    def centre_value(self,arr_val,a,inp):
        #print(inp)
        arr_val1 =0
        n=0
        list1 = []
        for x in a:
           n=n+1
           if n == arr_val:
               v=x
               print(v)
               break
        #print(v)
        if inp > v:        
           arr_val1 =len(a)-arr_val
           #list1 = []
           k=0
           for i in a:
               k=k+1
               if k > arr_val1:
                   list1.append(i)
           #print(list1)
        elif inp < v:
           arr_val1 = arr_val
           #list1 = []
           k=0
           for i in a:
               k=k+1
               if k < arr_val1:
                   list1.append(i)
           #print(list1)       
            
        
        return list1   
           
        
##    def compare_inp(self,a,centre_value,inp,centre):
##        if centre_value >= inp
           
        
        
a = 2,3,5,7,8,10,34
b1 = bin_search()
inp = 8
#print(b1)
while inp != a:
    find = b1.get_inp(a)
    centre = b1.find_centre(find)
    a = b1.centre_value(centre,a,inp)
    print(a)
    if inp == a:
        break
