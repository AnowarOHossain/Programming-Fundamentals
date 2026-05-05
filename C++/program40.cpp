#include <iostream>
#include <conio.h>
using namespace std;

int factorial(int n)
{
    if (n == 0)  // Base case should be n == 0
        return 1;    
    else
        return n * factorial(n - 1);
}

int main()
{
    cout << "Factorial of 5 = " << factorial(5) << endl;

    return 0;  // getch() is unnecessary in standard C++ execution
}
