a = int(input())

if a == 1:
    print("Invalid")

elif a>1:
    prime = True
    for i in range (2,int(a)):
        if a % i ==0:
            prime = False
            break
    
    if prime:
        print("Prime number")
    else:
        print("Not Prime")
