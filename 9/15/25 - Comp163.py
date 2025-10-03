#Append, Extend and Slice
fruits = ["apple","banana","cherry"]
fruits.append(["kiwi","pear"])
fruits.extend(["grape","plum"])
print(fruits[1:4])
print(fruits)

#Tuple Basics ("len" = length of tuple
fruits = ("banana,apple,cherry")
print(fruits[0])
print(len(fruits))

#Set Basics ("add" = adding a variable
colors = {"green", "red", "blue"}
colors.add(["yellow"])
print(colors)

#Dictionary Basics
student = {"name":"Ben", "age":29, "major": "computer eng."}

#Example of dictionary (Animal Kingdoms Types)
zoo_animals = ("lion, elephant, penguin, giraffe")
arctic_animals = {"penguin, seal, penguin, polar bear"}
bird_info = ("Animal: eagle, Wingspan: 3.2, Color: Golden")
animal_counts = {"Lions:":2, "Elephants:"4, "Penguins:"6,"Giraffes:"3}

#If Statements
temp = int(input)
if temp > 30:
    print("Its hot outside")

#If Else Statements
age = int(input)
if age >= 18:
    print("You are a adult.")
else:
    print("You are a minor.")

#Elif Statements
score = 85
if score >= 90:
    print("Grade is A")
elif score >= 80:
    print("Grade is B")
else score >= 70:
    print("Grade is C")

score = 85
if score >= 90:
    Grade = "A"
elif score >= 80:
    Grade = "B"
elif score >= 70:
    Grade = "C"
elif score >= 60:
    Grade = "D"
else:
    Grade = "F"
print(f"Your Grade is {Grade}.")

score = int(input)
if score >= 60:
    print("You passed")
else:
    print("Sorry, you did not pass the exam, Keep studying!")

# Logical Operators
# "and", "or", "not"
age = 17
has_id = True
is_student = False
gets_discount = age < 18 and has_id
special_pricing = is_student or age < 16
pays_full_price = not is_student

# Membership Operators
text = "Hello Python World!"
has_python = ("Python" in text)
no_java = ("Java" not in text)
has_o = ("o" in text)

# Identity Operators
# "is", "is not"
name = None
backup_name = "Guest"
list1 = [1, 2, 3]
list2 = list1
name_empty = name is None
backup_exists = backup_name is not None
same_list_object = list2 is list1

# Combining all three
sick_students = ["S123", "S234", "S345"]
assigned_bus = "BUS_A"
has_permission_slip = True
student_id = "S111"
student_bus = "BUS_A"
if (has_permission_slip = True and student_id is not sick_students)

# While Loops
count = 1
while count <= 5:
    print(count)
    count += 1

number = int(input())
while number < 1 or number > 10:
    print("Pick a valid number")
    number = int(input())
print("Valid number entered")

# For Loops (Lists = variable name / String = char / Tuple = number)
# Range Examples - range(2,8) = 2, 3, 4, 5, 6, 7
# Third number is step argument - range(1, 10, 2) = 1, 3, 5, 7, 9
for number in range(2, 12, 2):
    print(number)

number = input(int())
while True:
    number = input(int())
    if number == "Quit":
        break
    integer = int(number)
    if integer >0:
        print(integer)
    else:
        print("You printed a negative number.")

for number in range(1, 10):
    if number % 3 == 0:
        continue
    else:
        print(number)

#Git Commit 2
print("=== Challenge 2: Prime Number Checker ===")
integer = int(input())
print(f"Enter a number: Testing divisors from 2 to {integer - 1}...")
prime = True
for i in range(2, integer):
    if integer % i == 0:
        prime = False
        break
if prime:
    print(f"{integer} is prime!")
else:
    print(f"{integer} is not prime (divisible by 3)")
print()

#Git Commit 3
print("=== Challenge 3: Multiplication Table ===")
print("Multiplication Table:")
print("    ", end="")
#AI used to find out how to use "col" and "row" to print the table properly.
for col in range(1, 11):
    print(f"{col:4}", end="")
print()
for row in range(1, 11):
    print(f"{row:2} ", end="")
    for col in range(1, 11):
        product = row * col
        print(f"{product:4}", end="")
    print()







