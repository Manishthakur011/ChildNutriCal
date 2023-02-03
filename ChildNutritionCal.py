import math
Name = str(input("Enter the User Name :"))
Age  = int(input("Enter the User Age :"))
Height = int(input("Enter the User Height in inches :"))
Weight = int(input("Enter the User Weight in lbs :"))
#Calculating BMI
BMIvalue = float(Weight/(Height**2)*703)
BMIvalue = float(math.floor(BMIvalue*100)/100)
#CALORIE CONSUMPTION
#We take input from User as grams,convert it into calories and add them to get the total calories consumed by the User.
Milk = int(input("Milk(grams) : "))
Vegetables = int(input("Vegetables(grams) : "))
Vegetables = 0.85*Vegetables
Meat = int(input("Meat(grams) : "))
Meat = 1.43*Meat
Lentils = int(input("Lentils(grams) : "))
Lentils = 1.13*Lentils
Egg = int(input("Egg(grams) : "))
Egg = 1.55*Egg
Rice = int(input("Rice(grams) : "))
Rice =  1.3*Rice
together = int(Milk + Vegetables + Meat + Lentils + Egg + Rice)
#Using if and elif conditional statements
if BMIvalue < 16:
    print('BMI of '+Name+' is '+str(BMIvalue)+' and he(she) is Severely Underweight.')
elif BMIvalue >= 16 and BMIvalue < 18.5 :
    print('BMI of '+Name+' is '+str(BMIvalue)+' and he(she) is Underweight.')
elif BMIvalue >= 18.5 and BMIvalue < 25 :
    print('BMI of '+Name+' is '+str(BMIvalue)+' and he(she) is Healthy.')
elif BMIvalue >= 25 and BMIvalue < 30 :
    print('BMI of '+Name+' is '+str(BMIvalue)+' and he(she) is Overweight.')
elif BMIvalue >= 30 :
    print('BMI of '+Name+' is '+str(BMIvalue)+' and he(she) is Obese.')
if Age< 2 :
    if together>=800:
        print('The daily calorie consumption of '+Name+" is "+str(together)+' and he(she) is not undernourished.')
    else :
        print('The daily calorie consumption of of '+Name+" is "+str(together)+' and he(she) is undernourished.')
elif 2<=Age<4:
    if together>=1400:
        print('The daily calorie consumption of '+Name+" is "+str(together)+' and he(she) is not undernourished.')
    else :
        print('The daily calorie consumption of '+Name+" is "+str(together)+' and he(she) is undernourished.')
elif 4<=Age<8:
    if together>=1800 :
        print('The daily calorie consumption of '+Name+" is "+str(together)+' and he(she) is not undernourished.')
    else :
        print('The daily calorie consumption of '+Name+" is "+str(together)+' and he(she) is undernourished.')