# Java Complete Notes

**Author:** Anowar Hossain
**Subject:** Java Programming

---

## 1. Introduction to Java
* **Java:** Java is a high-level programming language originally developed by Sun Microsystems but currently owned by Oracle.
* **Features of Java:**
  * Platform independent (WORA - Write Once Run Anywhere).
  * Object-Oriented.
  * Support web-based applications.
  * Robust and Secure.
  * Multi-threaded.
* **JVM** = Java Virtual Machine
* **JDK** = Java Development Kit
* **IDE** = Netbeans / Eclipse / JDeveloper

**The Java Development Kit (JDK)** is a software development environment used for developing Java applications and applets. It includes the Java Runtime Environment (JRE), an interpreter/loader (Java), a compiler (javac), an archiver (jar), a documentation generator (Javadoc), and other tools needed in Java development.

Every Java program has at least one user-defined class.

**Class Declaration:**
```java
access_modifier class class_name {
    // body
}
```

### Java Keywords (48)
1. abstract 2. assert 3. boolean 4. break 5. byte 6. case 7. catch 8. char 9. class 10. continue 11. default 12. do 13. double 14. else 15. enum 16. extends 17. final 18. finally 19. float 20. for 21. if 22. implements 23. import 24. instanceof 25. int 26. interface 27. long 28. native 29. new 30. package 31. private 32. protected 33. public 34. return 35. short 36. static 37. strictfp 38. super 39. switch 40. synchronized 41. this 42. throw 43. throws 44. transient 45. try 46. void 47. volatile 48. while

### Basic Program Structure
```java
public class Main {
    public static void main(String[] args) {
        System.out.print("Anowar Hossain\n");
        System.out.print("01571169707");
    }
}
```

---

## 2. Escape Sequences & Comments
It is a special character followed by a backslash `\`.
* `\b` = backspace
* `\t` = tab
* `\n` = newline
* `\r` = carriage return
* `\"` = double quote
* `\'` = single quote
* `\\` = backslash

### Comments
Comments help to explain what the code is doing in your program. It helps the person reading the code more easily. Comments are ignored by the compiler.
1. **Single line comment:** `// Hello world program!`
2. **Multiline comment:** `/* Program name, Date etc. */`
3. **Documentational comment:** `/** ... */`

---

## 3. Java's Execution Steps & Datatypes
**Execution Steps:** 1. Edit  2. Compile  3. Load  4. Verify  5. Execute
*Source code (.java) -> Java compiler -> Byte code (.class) -> JVM -> Program Execution*

### Variable Declaration Syntax
`data_type variable_name;`

### Datatypes in Java
1. **Primitive:**
   * Boolean (`boolean`)
   * Numeric:
     * Character (`char`)
     * Integral: Integer (`byte`, `short`, `int`, `long`) and Floating point (`float`, `double`)
2. **Non-primitive:** `String`, `Array`, etc.

```java
public class Main {
    public static void main(String[] args) {
        boolean b = true;
        char c = 'a';
        short s = 32677;
        int i = 1256;
        float f = 10.2f;
        double d = 10.2;
        System.out.println("boolean b=" + b);
        System.out.println("c=" + c);
    }
}
```

### Format Specifiers
* `%c` = Character
* `%d` = Integer / Short
* `%.2f` = Float / Double

---

## 4. Input & Operators

### Getting Input from User
```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter Any Number: ");
        int number = input.nextInt();
        
        System.out.print("Enter your name: ");
        String name = input.nextLine(); // For strings
    }
}
```

### Arithmetic & Assignment Operators
* **Arithmetic:** `+`, `-`, `*`, `/`, `%`
* **Assignment:** `=`, `+=`, `-=`, `*=`, `/=`, `%=`
* **Unary:** `+x`, `-x`
* **Increment/Decrement:** `++a`, `a++`, `--a`, `a--`

### Conditional (Ternary) Operator
```java
int large = (num1 > num2) ? num1 : num2;
```

### Bitwise Operators
* `&` (AND), `|` (OR), `^` (XOR), `>>` (Right Shift), `<<` (Left Shift)

### Math Class
```java
int max = Math.max(x, y);
int min = Math.min(x, y);
int absolute = Math.abs(y);
double power = Math.pow(x, y);
int round = Math.round(8.4f);
double pi = Math.PI;
```

---

## 5. Control Statements

### if-else Example (Even/Odd)
```java
if (num % 2 == 0) {
    System.out.println("Even");
} else {
    System.out.println("Odd");
}
```

### switch Example
```java
switch (digit) {
    case 0:
        System.out.println("Zero");
        break;
    case 1:
        System.out.println("One");
        break;
    default:
        System.out.println("Not a digit");
}
```

---

## 6. Iteration / Looping
1. `for` loop
2. `while` loop
3. `do-while` loop

**Jump Statements:** `break`, `continue`, `return`.

### Sum of Digits
```java
int sum = 0, temp = num;
while(temp != 0) {
    int r = temp % 10;
    sum = sum + r;
    temp = temp / 10;
}
```

### Reverse a Number & Palindrome
```java
int sum = 0, temp = num;
while(temp != 0) {
    int r = temp % 10;
    sum = sum * 10 + r;
    temp = temp / 10;
}
if(num == sum) {
    System.out.println("Palindrome number");
}
```

### Armstrong Number
```java
int sum = 0, temp = num;
while(temp != 0) {
    int r = temp % 10;
    sum = sum + r * r * r;
    temp = temp / 10;
}
```

### Prime Number
```java
int count = 0;
for (int i = 2; i < num; i++) {
    if (num % i == 0) {
        count++;
        break;
    }
}
if (count == 0) System.out.println("Prime number");
```

### Fibonacci Series
```java
int first = 0, second = 1, fibo;
System.out.print(first + " " + second);
for (int i = 3; i <= n; i++) {
    fibo = first + second;
    System.out.print(" " + fibo);
    first = second;
    second = fibo;
}
```

---

## 7. Strings
```java
String s1 = "Anowar Hossain";
String s2 = new String("Anowar Hossain");

int len = s1.length();
boolean b = s1.equals(s2);
boolean c = s1.equalsIgnoreCase(s2);
boolean con = s1.contains("Hossain");
boolean e = s1.isEmpty();

String upperName = s1.toUpperCase();
String lowerName = s1.toLowerCase();
boolean start = s1.startsWith("An");

// Splitting
String[] s3 = s1.split(" ");
for(String x : s3) {
    System.out.println(x);
}
```

### StringBuffer & StringBuilder
```java
StringBuffer sb = new StringBuffer("Anowar");
sb.append(" Hossain");
sb.reverse();
sb.delete(0, 5);
sb.setLength(5);

StringBuilder str = new StringBuilder("Anowar");
str.append(" Hossain");
```

---

## 8. Wrapper Classes & Conversions
Wrapper classes are used to convert primitive into object and object into primitive.
* `int` -> `Integer`, `char` -> `Character`, etc.
* **Autoboxing:** Converting primitive to object.
* **Unboxing:** Converting object to primitive.

```java
int x = 30;
Integer y = Integer.valueOf(x); // Primitive to Object
Integer z = x; // Autoboxing

Double d = new Double(10.25);
double e = d; // Unboxing
```

### Number Conversions
```java
// Binary String to Decimal
String binary = "1010";
Integer decimal = Integer.parseInt(binary, 2);

// Decimal to Binary/Octal/Hexa String
String b = Integer.toBinaryString(15);
String o = Integer.toOctalString(15);
String h = Integer.toHexString(15);
```

### Random, Date & Time
```java
import java.util.Random;
Random rand = new Random();
int randomNumber = rand.nextInt(10) + 1; // 1 to 10

import java.util.Date;
import java.text.SimpleDateFormat;
Date date = new Date();
SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
String currentDate = dateFormat.format(date);

import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
LocalTime time = LocalTime.now();
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("hh:mm:ss");
```

---

## 9. Arrays
```java
int[] number = new int[5];
number[0] = 10;
int len = number.length;

// For-each loop
String[] names = {"Anowar", "Hamza", "Mridul"};
for (String x : names) {
    System.out.println(x);
}

// Sorting Array
import java.util.Arrays;
int[] num = {10, -3, 18, 5, 25};
Arrays.sort(num); // Ascending
```

### 2D Arrays & Matrices
```java
int[][] A = new int[2][3];
// Diagonal sum logic: if (row == col)
// Upper triangle logic: if (row < col)
// Lower triangle logic: if (row > col)
```

---

## 10. ArrayList
| Array | ArrayList |
| :--- | :--- |
| 1. Not Resizable | 1. Resizable |
| 2. for, for-each loop | 2. for-each loop, iterator |
| 3. Fast | 3. Slow |
| 4. array.length | 4. array.size() |

```java
import java.util.ArrayList;
import java.util.Collections;

ArrayList<Integer> number = new ArrayList<Integer>();
number.add(10);
number.add(3, 40); // index, value
number.remove(2);
number.clear();
boolean check = number.isEmpty();
int pos = number.indexOf(40);
number.set(3, 50); // replace
int x = number.get(0);

// Sorting
Collections.sort(number);
Collections.sort(number, Collections.reverseOrder());
```

---

## 11. Object-Oriented Programming (OOP)
**Core Concepts:** 1. Classes 2. Inheritance 3. Abstraction 4. Polymorphism 5. Access Modifiers 6. Interface 7. Encapsulation 8. Abstract class

* **Class:** A class is a blueprint or template from which individual objects are created.

```java
public class Teacher {
    String name, gender; // instance variables
    int phone;
    
    // Parameterized Method
    void setInformation(String n, String m, int ph) {
        name = n; gender = m; phone = ph;
    }
    void displayInformation() {
        System.out.println("Name: " + name);
    }
}
```

### Constructors
A constructor is a special type of method used to initialize the object.
* **Properties:** Same name as the class, no return type (not even void), called automatically.
* **Types:** Default constructor, Parameterized constructor, Overloading constructor.

### Static Keyword
Used for memory management. Relates to the class rather than the object.
* **Static Variable:** Not related to the object, related to the class.
* **Static Method:** Cannot use non-static members. `this` and `super` keywords cannot be used here.
* **Static Block:** Executed before the main method.

### Types of Variables
1. **Local:** Declared inside a method, constructor, or block.
2. **Instance:** Declared inside the class but outside any method.
3. **Class/Static:** Declared as static.

---

## 12. Methods & Passing Arguments
**Method Overloading:** A process that allows a class to have two or more methods having the same name, as long as their parameter declarations are different.

**Argument Passing:**
1. **Call-by-value:** Original value doesn't change. Changes to formal parameter don't affect actual parameter.
2. **Call-by-reference:** Passing a reference type data (object, array). Original value gets changed.

**Variable Length Arguments (Varargs):** A method that takes a variable number of arguments.
```java
void add(int... num) {
    int sum = 0;
    for(int x : num) sum = sum + x;
}
```

**Recursion vs Iteration:**
* **Recursion:** Uses selection structure (if, else). Terminates when base case is satisfied. Slower, smaller code.
* **Iteration:** Uses repetition structure (for, while). Terminates when continuation condition fails. Faster, bigger code.

---

## 13. Encapsulation
Encapsulation is a process of:
1. Packaging variables and methods into a single unit.
2. Protecting data by declaring them as private (Data hiding).

**How to achieve:**
* Declare variables as `private`.
* Provide `public` setter and getter methods.

---

## 14. Inheritance
The process where one class acquires the properties (methods and fields) of another.
* **Why?** Code reusability, Method overriding, Implement parent-child relationship.
* **Types:** 1. Single 2. Multilevel 3. Hierarchical 4. Multiple (Interfaces support this).

```java
public class Teacher extends Person {
    // inherits properties of Person
}
```

### Method Overriding
Declaring a method in a subclass which is already present in superclass. Used for runtime polymorphism.
* **Can we override static method?** No, static methods are bound to the class.
* **Can we override main method?** No, because main is a static method.

### Keywords
* **`super` keyword:** Used to refer immediate super class object. Calls super class instance variable, overridden method, or constructor.
* **`this` keyword:** Used to refer current class object. Calls current class instance variable, method, or constructor.
* **`final` keyword:** Restricts the user. `final` variable becomes constant, `final` method cannot be overridden, `final` class cannot be inherited.

---

## 15. Polymorphism
Polymorphism = Poly (many) + morphs (forms) -> many forms.
1. **Compile Time / Static:** Method Overloading, Constructor Overloading.
2. **Run Time / Dynamic:** Method Overriding.

---

## 16. Abstraction & Interfaces
**Abstraction** is the process of hiding the implementation details and showing only functionality to the user. Achieved via Abstract class (0 to 100%) or Interface (100%).

### Abstract Class
* Abstract method has no body, ends with a semicolon.
* Must be overridden in child class.
* Abstract class can have abstract and non-abstract methods.
* Cannot be instantiated.

### Interface
An interface is a collection of abstract methods.
* Supports multiple inheritance.
* Uses `implements` keyword.
* All methods in an interface are implicitly `public` and `abstract`.
* All variables are implicitly `public`, `static`, and `final`.

---

## 17. Packages & Access Modifiers
A package is a group of related classes, interfaces, and sub-packages.
* **Built-in:** `java.io`, `java.lang`, `java.util`, `java.awt`, `java.applet`.
* **User-defined:** e.g., `import myPackage;`

**Access Modifiers:** `private`, `default`, `protected`, `public`.

---

## 18. Type Casting
Converting one data type to another.
1. **Implicit (Widening):** `byte` -> `short` -> `int` -> `long` -> `float` -> `double`
2. **Explicit (Narrowing):** `double` -> `float` -> `long` -> `int` -> `short` -> `byte`
   ```java
   double y = 10.5;
   int x = (int) y;
   ```
3. **Object Type Casting:** Upcasting (child to parent), Downcasting (parent to child).

---

## 19. Exception Handling
An exception is an abnormal condition that arises in a code sequence at runtime.
* **Keywords:** `try`, `catch`, `finally`, `throw`, `throws`.

```java
try {
    int result = x / y; // ArithmeticException
} catch (Exception e) {
    System.out.println("Exception: " + e);
} finally {
    System.out.println("Block executed regardless of exception");
}
```
*Common Exceptions:* `ArithmeticException`, `NullPointerException`, `ArrayIndexOutOfBoundsException`, `NumberFormatException`, `FileNotFoundException`, `IOException`.

---

## 20. Collections Framework

### LinkedList
Manipulating data is fast (deleting or inserting). Can contain duplicate elements.
```java
LinkedList<String> list = new LinkedList<String>();
list.add("UAE");
list.addFirst("Australia");
list.remove("Japan");
```

### HashMap
```java
HashMap<Integer, String> customer = new HashMap<Integer, String>();
customer.put(101, "Anowar");
String name = customer.get(101);
```

### HashSet
```java
HashSet<String> fruits = new HashSet<String>();
fruits.add("Apple");
fruits.remove("Apple");
fruits.clear();
```

---

## 21. File Handling
```java
import java.io.File;
import java.util.Formatter;
import java.util.Scanner;

// Create Directory
File dir = new File("location_path");
dir.mkdir();

// Create File
File file = new File(dir.getAbsolutePath() + "/student.txt");
file.createNewFile();

// Write to File
Formatter formatter = new Formatter(file.getAbsolutePath());
formatter.format("%s %s \n", id, name);
formatter.close();

// Read from File
Scanner scanner = new Scanner(file);
while(scanner.hasNext()) {
    String id = scanner.next();
    String name = scanner.next();
    System.out.println("ID: " + id + " Name: " + name);
}
scanner.close();
```

## Handwritten Notes

I have documented my Java learning journey with handwritten notes. You can access the PDF here:

[📄 Java Handwritten Notes] (https://drive.google.com/file/d/19s3bAS2hL2_PO0p5hFIWmxSnyjXac0g2/view?usp=sharing)

