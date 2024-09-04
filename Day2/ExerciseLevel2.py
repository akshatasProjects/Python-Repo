#Exercises: Level 2
# Write a python comment saying 'Day 2: 30 Days of python programming'
first_name = "Akshata"
last_name = "Ajit"
full_name = "Akshata Ajit"
country = "India"
city = "Dharwad"
age = 36
year = 2024
is_married = True
is_true = False
is_light_on = True

first_name, last_name, city = "Atharva", "Jog", "Dharwad"

#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))

#Using the len() built-in function, find the length of your first name
print(len(first_name))

#Compare the length of your first name and your last name
first_name_len = len(first_name)
last_name_len = len(last_name)
print(min(first_name_len, last_name_len))

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

#Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

#The radius of a circle is 30 meters
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius = 30
area_of_circle = 3.142 * radius * radius 

#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * 3.142 * radius

# Take radius as user input and calculate the area.
radius_input = int(input("Enter the radius"))
area_of_circle = 3.142 * radius_input * radius_input 