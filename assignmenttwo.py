import datetime as dt
import math
# ====================================================================================
"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.
"""
# ====================================================================================
# Allow the two Names and age of a person to be captured
fname = input("Enter your First Name: ")
lname = input("Enter your last Name: ")
age = input("Enter your Age: ")
username = fname + " "+lname 

#compute the difference of the age and 100 and convert to days
diff = (100 - int(age))*365
year_diff = dt.timedelta(days=diff)
today = dt.date.today()
# Add the days to todays date before printing
cent_year = today + year_diff
print(f"Hello  {username }, You will turn 100 in the Year {cent_year.year}.")


# ====================================================================================
# Display the current date and time
# ====================================================================================
print(dt.datetime.now())


# ====================================================================================
# Code to perform Convertions 
# ====================================================================================
#Convert days to seconds
days = input("Enter the number of days to convert to Seconds: ")
seconds = int(days)*60*60*24
print(f"There are {seconds:,} seconds in {days} days")

#Convert Hours to Minutes
hours = input("Enter the number of hours to minutes: ")
minutes = int(hours)*60
print(f"There are {minutes:,} minutes in {hours} hours")


# ====================================================================================
# Code to calculate  BMI (Body Mass Index) 
# ====================================================================================
print("To calculaate your BMI")
weight = input("Enter your weight in Kilograms: ")
height = input("Enter your height in Meters: ")

comp = float(weight) / (float(height)*float(height))
bmi = round(comp,1)

if bmi < 18.5:
    print(f"{bmi} Your BMI is Underweight")
elif bmi >= 18.5 and bmi <= 25.0:
    print(f"{bmi} Your BMI is normal" )
elif bmi >= 25.0 and bmi <= 29.9:
    print(f"{bmi} Your BMI is Overweight" )
else:
    print(f"{bmi} Obese range")

 
# ====================================================================================
# Code to convert Fahrenheit to Celsius 
# ====================================================================================
print("To convert Fahrenheit to Celsius")
fahr = input("Enter Fahrenheit: ")
celsius = (float(fahr)-32)/1.8
print(f"{round(celsius,1)} Celsius") 