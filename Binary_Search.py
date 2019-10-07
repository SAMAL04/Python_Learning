import math
class bin_search:
    a = 2,3,5,7,8,10,34
#find 7 exists or not
    l = len(a)
    div_two = l/2
    ty_pe = type(div_two)

    def find_centre(ty_pe):
        if ty_pe ==  float:
            centre_element =math.ceil(div_two)
            print(centre_element)
        else:
            centre_element(div_two)
            print(centre_element)
        return centre_element
b1 = bin_search()
b1.find_centre(ty_pe)
