list_users = {
    "sat@guvi.in":"Sathiya@25",
    "hem@guvi.in":"Hemanika@26",
    "mal@guvi.in":"Malles@09"    
    }
print("Enter Username")
user_name = input()
print("Enter Password")
pass_wrd = input()
def user_val(user_name):
    for x,y in list_users.items():
        #print(x)
            if user_name == x:
                #print(user_name)
                if "@" and "in" not in user_name:
                    print("Username Wrong")
                    break


                break               
                
            else:
                print("Username Wrong")
                break
user_val(user_name)

def pass_val(user_name,pass_wrd):
    pwd = list_users.get(user_name)
    #print(pwd)
    if pwd ==pass_wrd:        
        for ch in pwd:
            regex = "[@_!#$%^&*()<>?/\|}{~:]" 
            a = ch.isalpha()
            if a == True:
                alp = True
                #print("A")
                #print(alp)
            b = ch.isdigit()
            if b == True:
                dig = True
                #print("N")      
                #print(dig)
            if ch in regex:
                c = True
                if c == True:
                    spe = True
                    #print("S")
                    #print(spe)
            else:
                c = False
            #print(c)    
        if alp == True and spe == True:
            print("Valid User")               
    else:
        print("Username\Password properties does not match")
pass_val(user_name,pass_wrd)
