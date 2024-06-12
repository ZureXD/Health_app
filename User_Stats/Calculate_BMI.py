#calculating BMI
def BMI(weight,height,age):
    BMI = weight/((height/100)*(height/100))
    return BMI

#Bmi Range for children
def Child_BMI_zone(BMI):
    if BMI <= 18.4:
        print("You are Underweight")
    elif 18.4 < BMI <= 24.9:
        print("You are Normal Weight")
    elif 24.9 < BMI <= 39.9:
        print("you are Overweight")
    elif BMI >39.9:
        print("You are Obese")
#Bmi range for Adults
def Adult_BMI_zone(BMI):
    if BMI <= 16:
        print("You are Severely Underweight")
    elif 16 < BMI <= 18.4:
        print("You are Underweight")
    elif 18.4 < BMI <= 24.9:
        print("you are Normal Weight")
    elif 24.9 < BMI <= 29.9:
        print("you are Overweight")
    elif 29.9 < BMI <= 34.9:
        print("you are Moderately Obese")
    elif 34.9 < BMI <= 39.9:
        print("you are Severely Obese")
    elif BMI >39.9:
        print("You are Morbidly Obese")

#checking BMI range
def BMI_calculation():
    while True:
        try:
            age = int(input("Enter age: "))
            height = float(input("Enter height: "))
            weight = float(input("Enter weight: "))
            break
        except ValueError:
            print("Invalid inputs, please enter valid arguments")
    
    bmi = BMI(weight,height,age)
    if age >= 20:
        Adult_BMI_zone(bmi)
    elif 0 < age < 20:
        Child_BMI_zone(bmi)
    else:
        print("Invalid age input")