#find 7 exists or not
import math
class bin_search:
    
    def get_inp(a):   
        l = len(a)
        div_two = l/2
        ty_pe = type(div_two)
        list_in =[div_two,ty_pe]
        return list_in

    def find_centre(find_inp):
        cen = div_two
        if ty_pe ==  float:
            centre_element =math.ceil(cen)
            print(centre_element)
        else:
            centre_element =cen
            print(centre_element)
        return centre_element
b1 = bin_search()
a = 2,3,5,7,8,10,34
find_in = b1.get_inp(a)
print(find_in)
print(a)
c = b1.ty_pe
print(c)
b1.find_centre(a, c)
