#include <iostream>
using namespace std;

class Teacher {
public:
    int id;
    string subject;

    Teacher(int t_id, string t_subject) {
        id = t_id;
        subject = t_subject;
    }

    void display() {
        cout << id << "  " << subject << endl;
    }
};

int main()
{
    cout << "ID" << "  " << "Subject" << endl;
    cout << "------------------"<< endl;

    Teacher t1(201, "Mathematics");
    t1.display();

    Teacher t2(202, "Physics");
    t2.display();

    return 0;
}
