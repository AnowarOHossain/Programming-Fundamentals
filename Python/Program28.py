# Dictionaries -> key, value
# name -anisul islam
# email - anisul2010s@yahoo.co.uk
# word - meaning

studentId = {
    # "101" : "Anowar Hossain",
    # "102": "Kazi Shah Hamza",
    # "103": "Shihab Sarkar",
    101: "Anowar Hossain",
    102: "Kazi Shah Hamza",
    103: "Shihab Sarkar",
}

print(studentId[101])
# print(studentId.get("101"))
print(studentId.get(103, "Not a valid key"))
print(studentId.get(106, "Not a valid key"))