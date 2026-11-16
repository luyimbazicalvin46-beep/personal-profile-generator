#---WELCOME---
print(" = " * 40)
print("PERSONAL PROFILE GENERATOR")
print(" = " * 40)
print( )
#---INPUT SECTION---
#Collect personal information from user
full_name = input("Enter your full our full name: ")
age = int( input("Enter your age: "))
height = float(input("Enter your height in metres: "))
weight = float(input("Enter your weight in kg: "))
city = input("Enter your city: ")
hobby = input("Enter your favorite hobby : ")
is_student = input("Are you a student?: ")

#---PROCESSING SECTION ---
# Calculate BMI
bmi = weight/(height ** 2)
# Calculate year of birth
birth_year = 2025 - age
#calculate approximate days lived
days_lived = age * 365
# Determine BMI category 
if bmi < 18.5 :
    bmi_category = "Underweight"
elif bmi < 25 :
    bmi_category = "Normal weight"
elif bmi < 30 :
    bmi_category = "Overweight"
else:
    bmi_category = "Obese"

#---OUT SECTION---
print( )
print(" = " * 40)
print(f"Name :    {full_name}")
print(f"Age :    {age} years old")
print(f"Born :    {birth_year}")
print(f"City :    {city}")
print(f"Hobby :    {hobby}")
print(f"Student :    {'Yes' if is_student else 'No'}")
print(" = " * 40)
print(f"Height :    {height:.2f} m")
print(f"Weight :    {weight:.1f} kg")
print(f"BMI :    {bmi:.1f} ({bmi_category})")
print(f"Days lived :    { days_lived : , }")
print(" = " * 40)
print(f"Hello {full_name.split( ) [0]} ! keep learning python !")
print(" = " * 40)
