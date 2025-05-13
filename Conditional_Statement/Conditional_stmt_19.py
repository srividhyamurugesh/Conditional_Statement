salary=int(input("Enter ur salary: "))
age=int(input("Enter ur age: "))
if(salary>=20000 or age<=25):
        loan=int(input("Enter req.loan amnt: "))
        if(loan<=50000):
            print("u r eligible for loan")
         
        else:
            print("not eligible")
       
else:
    print("Not eligible to apply for loan")
