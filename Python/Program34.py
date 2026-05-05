# xargs -> receive any number of parameters -> acts like tuples
def student(*details):
    print(details)
    print(details[1])


student(101, "Anowar Hossain")
student(101, "Shihab Sharkar", 3.92)

# xxargs -> receive any number of parameters -> acts like dictionaries -> key, value
def studentDetails(**details):
    print(details)
    print(details["id"])


studentDetails(id= 101,Name = "Anowar Hossain")