print("   Welcome to Python World!!!   ")


data = {}
 
with open("Login.txt","r") as test:
    lines=test.readlines()#all lines
    for line in lines: # slicing one line at a time
        n,p=line.strip().split(':') #split() using which we are splitting n & p
        data[n]=p # n= key , p=value in data dict

while True:
    ans=input("Enter your name to login :")

    if ans in data.keys():
        print("Hi",ans)
        in_p=input("Please type you password : ")#1234 
        if in_p.lower() == data[ans].lower():#data[ans]->dict[key]=value
            print("Welcome to python world")

            break
            
    
        else:
            
            print("Incorrect password")
    else:
        print("Invalid Username")

else:
    print("Please try entering one or 2")
