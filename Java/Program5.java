/*
 * Learning outcomes
 * format specifiers
 */
public class Program5 {
  public static void main(String[] args) {

    // declaring variables for a student
    String name;
    int id, age;
    double gpa;
    boolean isRegisted;

    // initializing variables for a student
    name = "Anowar Hossain";
    id = 221071051;
    age = 24;
    gpa = 3.62;
    isRegisted = true;

    // printing variables
    System.out.println("Student Information");
    System.out.println("--------------------");
    System.out.printf("Name: "+name);
    System.out.printf("Name: %s\n",name);
    System.out.printf("ID : %d: \n",id);
    System.out.printf("Age: %d\n",age);
    System.out.printf("GPA: %.2f\n",gpa);
    System.out.printf("Registered: %b\n",isRegisted);
  }
}
