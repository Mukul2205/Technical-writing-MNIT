#COMPUTING GROSS SALARY
grade=str(input("Enter Grade: "))
if grade=="A" or grade=="a":
    basic=10000
    hra=0.20*basic
    pf=0.11*basic
    allow=1700
    da=0.5*basic
    salary=basic+hra+allow+da-pf
    print("The salary is: ",salary)
elif grade=="B" or grade=="b":
    basic=4567
    hra=0.20*basic
    pf=0.11*basic
    allow=1500
    da=0.5*basic
    salary=basic+hra+allow+da-pf
    print("The salary is: ",salary)