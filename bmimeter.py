weight= float(input("enter your weight"))
height= float(input("enter your height in metres"))
a=weight/height**2
print(a)

if a>18.5 and a<30 :
 print("you are healthy")

elif a<18.5:
 print("you are underweight") 
elif a>30:
 print("you are overweight")
elif  a>32:
 print("you are obese")
 