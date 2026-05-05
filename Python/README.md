# Python Complete Notes

**Author:** Anowar Hossain
**Subject:** Python Programming

---

## 1. Introduction to Python
* **What is Python?** Python is a high-level programming language, interpreted, and object-oriented. It was created by Guido van Rossum, and released in 1991.
* **Python used for:**
  * Web Development, using the frameworks Django, Flask, Pylons.
  * Desktop applications with PyQt, Gtk, wxWidgets and many more.
  * Mobile applications using Kivy or BeeWare.
  * Data Science and Visualization using Numpy, Pandas and Matplotlib.
  * Machine Learning with Tensorflow and Scikit-learn.
  * Artificial Intelligence.

**Program: First python program**
```python
print("Anowar Hossain")
print(22102055)
```

**Program: Backslash characters and comments**
```python
# This is a single line comment
print("Anowar Hossain \n 01571169707")
print("\"Anowar Hossain\"")

'''
This is a comment
written in
more than just one line
'''
print("Its okay, I got it")
```
**Backslash character / Escape Sequences:**
* `\n` = new line
* `\t` = tab
* `\"` = "
* `\'` = '

---

## 2. Variables and Data Types
**Program: Variables and Data Types**
```python
name = "Anowar Hossain"
age = 21
cgpa = 3.83

print("Our new student name is " + name)
print(name + " lives in Dhaka")
print("He is currently", age, " years old")
print("At the age of ", age, ", he has started to learn Python")
print(name + " has scored", cgpa, " in the exam")

# String concatenation
print("Anowar" + "Hossain")
```

**Program: Basic Numerical Operations**
```python
a = 18
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b) # Floor
print(4 ** 2) # Exponentiation
```

---

## 3. Getting User Input & Type Casting
**Program: Getting User Input**
```python
name = input("Enter your name: ")
age = input("Enter your age: ")
gpa = input("Enter your gpa: ")

print("Name: " + name)
print("Age: " + age)
print("GPA: " + gpa)
```

**Program: Type casting**
```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 + num2
print("The result is", result)

result = num1 - num2
print("The result is", result)
```

---

## 4. Area of Shapes & Math Functions
**Program: Area of any shape**
```python
# Area of triangle
base = float(input("Enter Base = "))
height = float(input("Enter Height = "))
area = 0.5 * base * height
print("Area of triangle =", area)

# Area of circle
radius = float(input("Enter Radius = "))
area = 3.1416 * radius * radius
print("Area of circle =", area)
```

**Program: Math related library function**
```python
from math import *
print(max(20, 10))
print(min(20, 10))
print(abs(-4))
print(pow(2, 3))
print(sqrt(25))
print(round(3.8))
print(floor(3.7))
print(ceil(3.7))
```

---

## 5. Formatted String & Type Function
**Program: Formatted string, Type function**
```python
num1 = 20
num2 = 30
print(f"{num1} + {num2} = {num1 + num2}")

print("Anowar Hossain ", end="")
print("01571169707")

# Type function
print(type(25))
print(type(25.5))
print(type("Anowar"))
print(type(True))
```

---

## 6. Operators & Conditionals
**Program: Relational Operators and Boolean Data Types**
```python
print(30 > 20)
print(30 < 20)
print(30 >= 20)
print(30 <= 20)
print(30 == 20)
print(30 != 20)
print("Anowar" == "Anowar")
```

**Program: If...else statement**
```python
num = 5
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**Program: else if = elif statement**
```python
marks = 74
if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("A-")
elif marks >= 50:
    print("B")
elif marks >= 40:
    print("C")
elif marks >= 33:
    print("D")
else:
    print("Fail")
```

**Program: Inner if statement / nested if statement**
```python
num1 = 10
num2 = 20
num3 = 30

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
if num2 > num1:
    if num2 > num3:
        print(num2)
    else:
        print(num3)
```

**Program: Ternary Operator**
```python
num1 = 30
num2 = 50
max = num1 if num1 > num2 else num2
print("Maximum = ", max)
```

**Program: Logical Operators (and, or, not)**
```python
num1 = 20
num2 = 10
num3 = 80

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)
```

**Program: Logical operator (Vowel/Consonant)**
```python
ch = 'a'
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("Vowel")
else:
    print("Consonant")
```

---

## 7. Loops (While & For)
**Program: While loop**
```python
i = 1
while i <= 20:
    print(i)
    i = i + 1
print("Program End")
```

**Program: sum of n number**
```python
n = int(input("Enter the last term: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print(sum)
```

**Program: break & continue**
```python
i = 1
while i <= 100:
    if i == 20:
        break
    print(i)
    i = i + 1
print("Hello")

# Continue
i = 1
while i <= 100:
    if i == 20:
        continue
    print(i)
    i = i + 1
```

**Program: For loop**
```python
num = [10, 20, 30, 40, 50]
for x in num:
    print(x)

# Sum
sum = 0
for x in num:
    sum = sum + x
print(sum)
```

---

## 8. Lists & Range
**Program: List-1**
```python
subjects = ["C", "C++", "Java", "Python", "JS"]
print(subjects)
print(subjects[0])
print(subjects[2:])
print(subjects[-1])
print("Swift" in subjects)
print("Swift" not in subjects)
print(subjects + ["Swift", 27])
```

**Program: List-2**
```python
subjects = ["C", "C++", "Java", "Python", "JS"]
print(len(subjects))
subjects.append("OS")
subjects.insert(2, "OS")
subjects.remove("JS")
subjects.sort()

subjects = [20, 10, 4, 55]
subjects.reverse()
subjects.pop()
subjects2 = subjects.copy()
pos = subjects.index(4)
pos = subjects.count(4)
subjects.clear()
```

**Program: Range**
```python
num = list(range(10))
print(num[2])

num = list(range(5, 11))
num = list(range(2, 101, 2))
```

---

## 9. Series & Patterns
**Series Programs:**
```python
# 1 + 2 + 3 + ... + n
n = int(input("Enter the last number: "))
sum = 0
for x in range(1, n + 1, 1):
    sum = sum + x
print(sum)

# 2 + 4 + 6 + ... + n
for x in range(2, n + 1, 2):
    sum = sum + x

# 1^2 + 2^2 + 3^2 + ... + n^2
for x in range(1, n + 1, 1):
    sum = sum + (x * x)

# 1 x 2 x 3 x ... x n
sum = 1
for x in range(1, n + 1, 1):
    sum = sum * x
```

**Program: Patterns**
```python
# Pattern 1 (Right Triangle)
n = 4
for i in range(n + 1):
    print(i * "*")

# Pattern 2 (Odd Stars)
n = 3
for i in range(n + 1):
    print((2 * i - 1) * "*")
```

---

## 10. Games & User Input (Advanced)
**Program: Guessing Game**
```python
from random import randint
for x in range(1, 6):
    guessNumber = int(input("Enter your guess between 1 to 5: "))
    randomNumber = randint(1, 5)
    if guessNumber == randomNumber:
        print("You have won")
    else:
        print("You have lost")
        print("Random number was:", randomNumber)
```

**Program: List as input from user**
```python
numOfWords = 0
numOfLetters = 0
numOfDigits = 0

text = input("Enter a text of number: ")
for x in text:
    x = x.lower()
    if x >= 'a' and x <= 'z':
        numOfLetters = numOfLetters + 1
    elif x >= '0' and x <= '9':
        numOfDigits = numOfDigits + 1
    elif x == ' ':
        numOfWords = numOfWords + 1

print("Number of Letters:", numOfLetters)
print("Number of Digits:", numOfDigits)
print("Number of Words:", numOfWords + 1)
```

---

## 11. Data Structures (Matrix, Dict, Tuple, Set)
**Program: Matrix**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix[0][2] = 10
print(matrix[0][2])

for row in matrix:
    for col in row:
        print(col)
```

**Program: Dictionaries**
```python
studentId = {
    101: "Anowar",
    102: "Hamza",
    103: "Soriful"
}
print(studentId.get(104, "Not a valid key"))
```

**Program: Tuples** (Immutable)
```python
students = (
    ("Anowar", 21, 3.75),
    "Hamza",
    "Masum"
)
print(students[0])
```

**Program: Set**
```python
num1 = {1, 2, 3, 4, 5}
num2 = set([4, 5, 6])
num2.add(7)
num2.remove(7)
print(4 in num2)

# Set Operations
print(num1 | num2) # Union
print(num1 & num2) # Intersection
print(num1 - num2) # Difference
```

---

## 12. Stack & Queue
**Program: Stack (LIFO)**
```python
books = []
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")
books.pop()
```

**Program: Queue (FIFO)**
```python
from collections import deque
bank = deque(["Anowar", "Toma", "Hamza"])
bank.popleft()
if not bank:
    print("No person left")
```

---

## 13. Functions
**Program: Introduction to Function**
```python
def add(x, y):
    sum = x + y
    print(sum)

add(10, 20)

# Returning value
def large(a, b):
    if a > b:
        return a
    else:
        return b
print(large(100, 30))
```

**Program: `*args` and `**kwargs`**
```python
# *args
def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

# **kwargs
def student(**details):
    print(details)
student(id=101, name="Anowar")
```

---

## 14. Advanced Functions (Lambda, Map, Filter)
**Lambda Function:** A function without a name (Anonymous function). Not as powerful as a Named Function. Works with a single expression.
```python
a = (lambda a, b: a*a + 2*a*b + b*b)(2, 3)
print(a)
```

**Map Function:**
```python
def square(x):
    return x ** 2
num = [1, 2, 3, 4, 5]
result = list(map(square, num))
```

**Filter Function:**
```python
num = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, num))
```

**List Comprehensions:**
```python
num = [1, 2, 3, 4, 5]
result = [x * x for x in num]
result_even = [x for x in num if x % 2 == 0]
```

**Zip Function:**
```python
roll = [101, 102, 103, 104]
name = ["Anowar", "Hamza", "Masum", "Ayman"]
print(list(zip(roll, name)))
```

**Recursion:**
```python
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
```

---

## 15. File Handling & Exceptions
**Program: Reading/Writing a File**
```python
file = open("student.txt", "r+")
text = file.read()
# Or: text = file.readlines()
# Or: for line in file: print(line)
file.close()

# Writing / Appending
file = open("student.txt", "w") # Overwrite
file.write("I am Hamza")
file.close()

file = open("student.txt", "a") # Append
file.write("\n I am Anowar")
file.close()
```

**Program: Exceptions Handling**
```python
try:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    result = num1 / num2
    print(result)
except (ValueError, ZeroDivisionError):
    print("Incorrect input.")
finally:
    print("Thanks")
```

**Program: Raising Exception**
```python
def voter(age):
    if age < 18:
        raise ValueError("Invalid Voter")
    return "You are allowed to vote"
```

---

## 16. Object-Oriented Programming (OOP)
**Program: Class, Objects & Methods**
```python
class Student:
    roll = ""
    gpa = ""

    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

rahim = Student()
rahim.set_value(101, 3.75)
rahim.display()
```

**Program: Constructor (`__init__`)**
```python
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        area = 0.5 * self.base * self.height
        print("Area = ", area)

t1 = Triangle(10, 20)
t1.calculate_area()
```

---

## 17. Inheritance & Polymorphism
**Program: Inheritance & Method Overriding**
```python
class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("I am area method of shape class")

class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of Triangle:", area)

t1 = Triangle(20, 30)
t1.area()
```

**Types of Inheritance:**
1. Hierarchical Inheritance
2. Multi-Level Inheritance
3. Multiple Inheritance

```python
# Multiple Inheritance Example
class A:
    def display(self):
        print("I am inside A class")

class B:
    def display(self):
        print("I am inside B class")

class C(A, B):
    def display(self):
        super().display() # Depending on MRO
        print("I am inside C class")
```

**Program: Abstraction**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of Triangle:", area)
```

**Program: Polymorphism**
```python
# Built in Polymorphic function
print(len("Anowar Hossain"))
print(len([10, 20, 30]))

# User defined Polymorphic function
def add(x, y, z=0):
    return x + y + z
```

---

## 18. Magic Methods
Magic methods for comparisons:
* `lt` for `<`
* `le` for `<=`
* `eq` for `==`
* `ne` for `!=`
* `gt` for `>`
* `ge` for `>=`

Magic methods for arithmetic: `__add__`, `__sub__`, `__mul__`, `__div__`.

**Program: Magic method (`__str__` & `__eq__`)**
```python
class Bike:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __eq__(self, other):
        return self.name == other.name and self.color == other.color

    def __str__(self):
        return f"Name={self.name}, Color={self.color}"

bike1 = Bike("Yamaha R15", "Blue")
bike2 = Bike("Yamaha R15", "Blue")

print(str(bike1))
print(bike1 == bike2) # Returns True due to __eq__
```

---

## 19. Modules & Regular Expressions
**Program: Creating your own Module**
```python
# area.py
def triangle_area(b, h):
    print(f"Area of Triangle is: {0.5 * b * h}")

# test.py
from area import triangle_area
triangle_area(10, 20)
```

**Regular Expression (Regex):**
Tools for manipulating string. Used for verifying string patterns and performing substitutions. Access via `re` module.
* `match()`: matches at the beginning of a string.
* `search()`: finds a match anywhere in the string.
* `findall()`: returns a list of all substrings that match a pattern.
* `re.sub(pattern, replacement, text)`: Search and Replace.

**Meta characters:**
* `.` (any character)
* `^` (starts with)
* `$` (ends with)
* `*` (0 or more)
* `+` (1 or more)
* `?` (0 or 1)
* `{and}` (curly braces for specific repetition)
* `[A-Z][a-z][0-9]` (Character classes)

**Program: Regex Search**
```python
import re
pattern = r"Colour"
if re.search(pattern, "Colour is Red, I like Blue"):
    print("Match")
```
## Handwritten Notes

I have documented my Python learning journey with handwritten notes. You can access the PDF here:

[📄 Python Handwritten Notes] (https://drive.google.com/file/d/1cxQYoizG1AeDPZB0x_0R85xbaFZ3t8Hg/view?usp=sharing)
