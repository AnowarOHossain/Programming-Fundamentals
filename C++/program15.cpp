#include <iostream>
#include <conio.h>
using namespace std;

int main()
{
    int number;

    cout << "Enter a number: ";
    cin >> number;  // Taking input from the user

    if (number > 0)
    {
        cout << "Positive" << endl;
    }
    else if (number < 0)
    {
        cout << "Negative" << endl;
    }
    else
    {
        cout << "Zero" << endl;
    }

    getch();
}
