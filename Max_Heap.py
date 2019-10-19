def add(a,insert):
    List =[]
    for x in a:
        List.append(x)
    List.append(insert)
    return List   
  
def root(List,insert):   
    s=0
    for n in List:
        s = s+1
        if n == insert:
            break            

    ind =s-1
    #insert = List[ind]
    root1 = (ind-1)//2
    root_ele = List[root1]
    if insert > List[root1]:
        List[root1] =insert
        List[ind] = root_ele
    #print(List)
    if List[0] < insert:
        root(List,insert)
        print(List)
list  = [9,7,6,4,2,3]
insert = 10
s = add(list,insert)
root(s,insert)
#list has been inserted with 10 which has to max-heap insertion
