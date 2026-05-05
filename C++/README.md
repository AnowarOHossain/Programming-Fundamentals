# Complete C++ Programming Notes

**Author:** Anowar Hossain
**Subject:** C++

---

## 1. Introduction to C++
* **What is C++?** C++ is known to be a very powerful computer programming language. It is a general-purpose, case-sensitive, object-oriented programming language.
* **Usage of C++:** It is used to develop game engines, games, desktop apps, art applications, music players, etc. It is highly used to write device drivers and other software.
* **History of C++:** C++ programming language was developed in 1980 by Bjarne Stroustrup at Bell Laboratories of AT&T. Bjarne Stroustrup is known as the founder of the C++ language. C++ was derived from C, and largely based on it. It is a Mid-level programming language.
* **Features of C++:** Simple, Rich Library, Fast Speed, Memory Management, Pointers, Recursion, Object Oriented, Compiler based.

**Required Softwares:**
* **Integrated Development Environment (IDE):** Provides tools for writing source code. Any text editor can be used as an IDE. Example: Code::Blocks, TurboC++ etc.
* **Compiler:** Compiles source code into the final executable program. The most frequently used and free available compiler is the GNU C/C++ compiler (MinGW).

---

## 2. Basic C++ Program Structure
```cpp
#include <iostream>
using namespace std;
int main() {
    cout << "Hello world!";
    return 0;
}
```
* `iostream` = input output stream একটি হেডার ফাইল। `#include` এর সাহায্যে এটি প্রোগ্রামে সংযুক্ত করা হয়।
* কম্পাইল এবং নির্বাহের সময় C/C++ প্রোগ্রাম `main()` ফাংশন থেকে শুরু হয়। তাই প্রোগ্রামে এ ফাংশন অবশ্যই লিখতে হয়। একটি প্রোগ্রামে একের অধিক ফাংশন থাকতে পারে, তবে `main` ফাংশন থাকা বাধ্যতামূলক।
* `cout <<` হচ্ছে standard output stream. এই কমান্ডের মাধ্যমে মনিটরে কোন কিছু প্রদর্শন/প্রিন্ট করা হয়।
* `return` হচ্ছে একটি keyword. Returning `0` means a successful termination.

**Printing multiple lines:**
```cpp
#include<iostream>
using namespace std;
int main() {
    cout << "Anowar Hossain\n";
    cout << "Mymensingh\n";
    cout << "01571169707";
    return 0;
}
// Or using endl:
// cout << "Anowar Hossain" << endl << "Mymensingh" << endl << "01571169707";
```

---

## 3. Tokens, Keywords, and Variables
**C++ Tokens:** 1. Keywords 2. Identifier 3. Constants 4. Strings 5. Special symbols 6. Operators

**Keywords:** Keywords (also known as reserved words) have special meaning to the C++ compiler and are always written typed in short (lower) cases.
* **32 keywords from C:** `auto`, `break`, `case`, `char`, `const`, `continue`, `default`, `do`, `double`, `else`, `enum`, `extern`, `float`, `for`, `goto`, `if`, `int`, `long`, `register`, `return`, `short`, `signed`, `sizeof`, `static`, `struct`, `switch`, `typedef`, `union`, `unsigned`, `void`, `volatile`, `while`.
* **30 keywords specific to C++:** `asm`, `bool`, `catch`, `class`, `const_cast`, `delete`, `dynamic_cast`, `explicit`, `false`, `friend`, `inline`, `mutable`, `namespace`, `new`, `operator`, `private`, `protected`, `public`, `reinterpret_cast`, `static_cast`, `template`, `this`, `throw`, `true`, `try`, `typeid`, `typename`, `using`, `virtual`, `wchar_t`.

*Keyword ব্যবহারের নিয়ম:*
* Keyword কখনও variable বা চলকের নাম হিসাবে ব্যবহার করা যায় না।
* Keyword এর প্রতিটি বর্ণ ছোট হাতের হয়। যেমন: `Int` (Invalid), `int` (Valid)।
* কখনও যদি দুইটি keyword একত্রে ব্যবহার করা হয়, তবে তাদের মধ্যে ফাঁকা স্থান থাকে। যেমন: `long double` (Valid).

*ভেরিয়েবল লেখার নিয়মগুলো:*
* ভেরিয়েবলের নামের মধ্যে বর্ণ (A...Z, a...z), অঙ্ক (0...9), আন্ডারস্কোর (_), ডলারচিহ্ন ($) ব্যবহার করা যায়।
* ভেরিয়েবলের নাম ডিজিট বা অঙ্ক দিয়ে শুরু হতে পারেনা।
* কোনো কিওয়ার্ড, ফাংশন ভেরিয়েবলের নাম হিসাবে ব্যবহার করা যায় না।
* ভেরিয়েবলের নামের মধ্যে কোনো ফাঁকা স্থান থাকতে পারে না।
* ভেরিয়েবলের নামকরণে সর্বাধিক ৩১ ক্যারেক্টার ব্যবহার করা যায়। তবে ৮ ক্যারেক্টার ব্যবহার করাই শ্রেয়।

---

## 4. Datatypes & Input/Output
**C++ Datatypes:**
1. User-defined type: Structure, Union, Class, Enumeration.
2. Built-in-type: Integral type (`int`, `char`), `void`, Floating type (`float`, `double`).
3. Derived type: Array, Function, Pointer.

**Program: Variables and String**
```cpp
#include<iostream>
using namespace std;
int main() {
    int num1 = 10, num2 = 20;
    char ch = 'A';
    cout << "Number1 = " << num1 << endl << "Number2 = " << num2 << endl;
    cout << "Character = " << ch;

    char name[14] = "Anowar Hossain";
    cout << "My name is = " << name;
    return 0;
}
```

**Program: Getting user input**
```cpp
#include<iostream>
using namespace std;
int main() {
    int num;
    cout << "Enter an integer number: ";
    cin >> num;
    cout << "Entered number is: " << num;
    return 0;
}
```

There are 4 datatype modifiers in C++: 1. `signed` 2. `unsigned` 3. `long` 4. `short`.

---

## 5. Operators & Math Formulas
**Operators:**
1. Arithmetic: `+`, `-`, `*`, `/`, `%`
2. Assignment: `=`, `+=`, `-=`, `*=`, `/=`
3. Relational: `<`, `>`, `<=`, `>=`, `==`
4. Logical: `&&`, `||`, `!`
5. Conditional (Ternary): `? :`
6. Bitwise: `&`, `|`, `^`, `<<`, `>>`
7. Unary: `++`, `--`, `+`, `-`
8. Special: comma (`,`), pointer (`*`), `sizeof()`

**Program: Formatting output & Type casting**
```cpp
#include<iostream>
#include<iomanip>
using namespace std;
int main() {
    float num1, num2;
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;
    
    cout << showpoint;
    cout << fixed;
    cout << setprecision(2);
    
    float sum = num1 + num2;
    cout << setw(20) << "Sum is: " << sum << endl;
    
    double div = (float) num1 / num2; // type casting
    cout << setw(20) << "Division is: " << div << endl;
    return 0;
}
```

**Math Formulas:**
* Area of triangle = `0.5 * base * height`
* Rectangle Area = `width * height`
* Circle Area = `pi * r * r` (Circumference = `2 * pi * r`)
* Parallelogram Area = `base * vertical height`
* Trapezium Area = `0.5 * (a + b) * h`
* Fahrenheit = `1.8 * Celsius + 32`

---

## 6. Control Statements (if-else, switch)
Any meaningful expression is called a statement.
* **Selection:** `if`, `else`, `else if`, `switch`
* **Iteration/Looping:** `for`, `while`, `do-while`
* **Jump:** `break`, `continue`, `return`

**Program: if...else if...else (Letter Grade)**
```cpp
#include <iostream>
using namespace std;
int main() {
    int mark;
    cout << "Enter Mark: ";
    cin >> mark;
    if (mark > 100 || mark < 0) {
        cout << "Invalid Mark";
    } else if (mark >= 80) {
        cout << "A+";
    } else if (mark >= 70) {
        cout << "A";
    } else {
        cout << "Fail";
    }
    return 0;
}
```

**Program: Switch (Digit spelling)**
Switch statement provides a better alternative than a large series of if-else statements.
```cpp
#include <iostream>
using namespace std;
int main() {
    int digit;
    cout << "Enter a digit: ";
    cin >> digit;
    switch(digit) {
        case 0: cout << "Zero"; break;
        case 1: cout << "One"; break;
        default: cout << "Not a valid digit";
    }
    return 0;
}
```

---

## 7. Loops (for, while, do-while)
A loop statement allows us to execute a statement or group of statements multiple times.

**for loop:**
```cpp
for(int i = 1; i <= 10; i++) {
    cout << "Bangladesh: " << i << endl;
}
```

**while loop:**
```cpp
int i = 1;
while(i <= 10) {
    cout << i << endl;
    i++;
}
```

**do-while loop:**
The do-while loop will execute at least one time even if the condition is false.
```cpp
int i = 1;
do {
    cout << i << endl;
    i++;
} while(i <= 10);
```

**Jump Statements:**
* `break`: Breaks the current flow of the program at a specified condition (breaks loop or switch).
* `continue`: Skips the current iteration of a loop.

---

## 8. Arrays (1D & 2D)
**1D Array:**
```cpp
#include<iostream>
using namespace std;
int main() {
    int marks[5] = {55, 45, 95, 47, 85};
    for(int i = 0; i < 5; i++) {
        cout << marks[i] << " ";
    }
    return 0;
}
```

**2D Array:**
```cpp
#include <iostream>
using namespace std;
int main() {
    int A[3][4] = {{5,6,7,8}, {9,10,11,12}, {13,14,15,16}};
    for (int row = 0; row < 3; row++) {
        for (int col = 0; col < 4; col++) {
            cout << A[row][col] << " ";
        }
        cout << endl;
    }
    return 0;
}
```

---

## 9. Pointers
**Program: Pointer Basics**
```cpp
#include <iostream>
using namespace std;
int main() {
    int x = 5;
    int *p;
    p = &x;
    cout << x << endl;   // Prints 5
    cout << &x << endl;  // Prints memory address of x
    cout << p << endl;   // Prints memory address of x
    cout << *p << endl;  // Prints 5
    return 0;
}
```

---

## 10. Functions & Recursion
A function is a group of statements that perform a particular task. If you need to do the same thing again and again, use a function.
**Types:** 1. Library Function 2. User-defined function
**Advantages:** 1. Code Reusability 2. Use the same function for different inputs.

**Program: Function Declaration and Calling**
```cpp
#include <iostream>
using namespace std;
void addition(int a, int b) {
    int sum = a + b;
    cout << "Sum=" << sum << endl;
}
int main() {
    addition(10, 20);
    return 0;
}
```

**Function Overloading:** Declaring multiple functions with the same name but different parameters.
```cpp
void sum(int x, int y) { int add = x + y; cout << add << endl; }
void sum(int x, int y, int z) { int add = x + y + z; cout << add << endl; }
```

**Recursion:** A process where a function can call itself. Needs a base case.
```cpp
int fact(int n) {
    if (n == 1) return 1;
    else return n * fact(n - 1);
}
```

**Passing Arguments:**
1. **Pass by value:** `void display(int num)` -> Passing a copy.
2. **Pass by reference:** `void display(int *num)` -> Passing address, modifies original value.

---

## 11. Strings & Scope Resolution Operator
**Strings:**
* C-style character string: `char name[30]; gets(name);`
* String Library `<cstring>`: `strlen()`, `strcpy()`, `strcat()`, `strupr()`, `strlwr()`, `strcmp()`.
* String class `<string>`: `string str1 = "Anowar";`

**Scope Resolution Operator (`::`):**
Used to access global variables when a local variable has the same name.
```cpp
int x = 10; // global
int main() {
    int x = 50; // local
    cout << ::x << endl; // Prints 10 (global)
    return 0;
}
```

---

## 12. Object Oriented Programming (OOP)
**OOP Concepts:** 1. Class 2. Object 3. Inheritance 4. Encapsulation 5. Polymorphism 6. Abstraction

* **Class:** A class is a template from which individual objects can be created.
* **Object:** Any class type variable is called an object.

**Program: Class & Object**
```cpp
#include <iostream>
using namespace std;
class Student {
public:
    int id;
    double gpa;
    void display() {
        cout << id << " " << gpa << endl;
    }
    void setValue(int x, double y) {
        id = x;
        gpa = y;
    }
};
int main() {
    Student Anowar;
    Anowar.setValue(102, 3.82);
    Anowar.display();
    return 0;
}
```

**Constructors:** A special type of function used to initialize the object. Has the same name as the class, no return type, and is called automatically. (Types: Default, Parameterized).

---

## 13. Encapsulation & Inheritance
**Encapsulation:** The process of combining variables and functions in a single unit (Class) and protecting data by declaring them as Private (Data Hiding). Private data can only be accessed through public functions (Setters and Getters).

**Inheritance:** The process of obtaining the data members and functions from one class to another class.
* **Importance:** Code reusability, less development time, less memory.
* **Types:** Single, Multilevel, Hierarchical, Multiple, Hybrid.

```cpp
class Person {
public:
    string name;
    int age;
};
class Student : public Person {
public:
    int id;
};
```

---

## 14. Polymorphism & Abstraction
**Polymorphism:** Poly (many) + morphism (forms) = many forms.
1. Compile time polymorphism / static binding (e.g., Function overloading).
2. Runtime Polymorphism / dynamic binding (e.g., Function overriding using `virtual` keyword).

**Function Overloading vs Overriding:**
* Overloading: Parameters must be different, occurs within the same class.
* Overriding: Parameters must be the same, occurs between super class and sub class (Inheritance is involved).

**Abstraction:** The process of hiding the implementation details and showing only the functionality to the user.
* **Properties of Abstract class:** Contains at least one pure virtual function (e.g., `virtual void sendMessage() = 0;`). Objects of an abstract class cannot be created.

---

## 15. Friend Class & Function Templates
**Friend Class:** Can access private members of another class.
```cpp
class A {
private:
    int id = 101;
    friend class B;
};
```

**Function Templates:** Used to create a generic function that can handle different data types.
```cpp
template <class myTemplate>
myTemplate add(myTemplate a, myTemplate b) {
    return a + b;
}
// Usage: add(10, 20) or add(10.5, 20.5)
```

---

## 16. Exception Handling
Exception Handling is a mechanism that can handle the exception (Runtime Errors). Keywords: `try`, `catch`, `throw`.

```cpp
#include <iostream>
using namespace std;
int main() {
    try {
        int num1, num2;
        cin >> num1 >> num2;
        if (num2 == 0) {
            throw -1;
        }
        double result = (double)num1 / num2;
        cout << "Result: " << result << endl;
    } catch(int x) {
        cout << "Divide by zero is not possible!" << endl;
    }
    return 0;
}
```

---

## 17. File Handling
File is used to store data permanently. Requires `<fstream>` library.
* `ofstream`: Data type used to create and write information to files.
* `ifstream`: Data type used to read information from files.

**Program: File Create, Write & Append**
```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    string name;
    // open file for writing/appending
    ofstream file;
    file.open("student.txt", ios::out | ios::app);
    
    cout << "Enter your name: ";
    getline(cin, name);
    file << "Welcome " << name << endl;
    
    file.close();
    cout << "Data is stored" << endl;
    return 0;
}
```

**Program: How to read from a file**
```cpp
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    string line;
    ifstream file("student.txt");
    
    while(getline(file, line)) {
        cout << line << endl;
    }
    file.close();
    return 0;
}
```
## Handwritten Notes

I have documented my learning journey for both C and C++ with handwritten notes. You can access the PDFs here:

- [📄 C Handwritten Notes] (https://drive.google.com/file/d/1Rv3vTeKcBRJeXfxGQF5epCH7NVTWPSU8/view?usp=sharing)   

- [📄 C++ Handwritten Notes] (https://drive.google.com/file/d/1CwhD5lElETOSAkqO6JGjiYtWtvnHlDRn/view?usp=sharing)
