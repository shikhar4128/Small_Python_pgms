#The Body Mass Index or BMI is calculated from weight and height of a Person.
#This python script displays the BMI based on user input .

height=int(input("Enter your height in centimeters: "))
weight=int(input("Enter your Weight in Kg: " ))

height=height/100
BMI=weight/(height*height)
print(f'your Body Mass Index is: {BMI}')

if BMI > 0:
    if BMI <=16:
        print("you are severely underweight")
    elif BMI <=18.5:
        print("you are underweight")
    elif BMI <=25:
        print("you are Healthy")
    elif BMI <=30:
        print("you are overweight")
    else:
        print("you are severely overweight")
else:
    print("Please enter valid details")