def gcd(a,b):
  
    gcd = []
    if  a < b:
        small = a
    else:        
        small = b
    for i in range(1,small+1):
        if ((a%i == 0) and (b%i == 0)):
            gcd.append(i)
    return(gcd)  

m = 12
n = 16
if (int(m) and int(n)):
    a=gcd(m,n)
    for c in a:
        print(c)
else:
    print("The value should be integer")
