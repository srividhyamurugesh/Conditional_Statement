a=int(input())
n=a%2
if(n==0):
    if(a>=3 and a<=5):
        print("Weird")
    elif(a>=6 and a<=20):
        print("Not Weird")
    else:
        print("Weird")
else:
    print("Weird")
