#Section 1
name = "Carlos"
age = 42
height = 5.7
is_student = True
print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#Section 2
name = input("What is your name?")
birth_year = int(input("Year of birth? "))
year = 2026
age = year - birth_year
print(f"Hi, {name} You are approximately {age} years old.")

#Section 3
number1 = float(input("Enter a first number to multiply:"))
number2 = float(input("Enter a second number to multiply: "))
total = number1 * number2
print(f"The total is {total} ")

#Section 4
line = "====================="
line2 = "---------------------"
receipt = "RECEIPT"
product = "Book"
price = float ("3.47")
quantity = int ("5")
print (line)
print (receipt)
print (line)
print (f"Product:{product}")
print (f"Price:$ {price}")
print (f"Quantity:{quantity}")
print (line2)
total = price * quantity
print(f"TOTAL: ${total}")
print (line)

#Section 5
name = input("What is your name?")
hometown = input("What is your hometown?")
hobby = input("What is your Hobby?")
fun_fact = input("What’s a fun fact about you?")
birth_year = int(input("Year of birth?"))
year = 2026
age = year - birth_year
line = "======================="
line2 = "-----------------------"
print (line)
print (f"Name:{name}")
print (line)
print (f"Hometown:{hometown}")
print (f"Hobby:{hobby}")
print (f"Fun fact:{fun_fact}")
print(f"Age:{age}")
print(line2)
