courses = ["MIT", "Cyber Security", "Data Science"]
print(courses)
#accesing an element
print(courses[2])

#looping through an array
for x in courses:
    print("course is" , x)
#adding a new element in an array
courses.append("Laravel")
print(courses)

#removing an element

courses.remove("Cyber Security")
print(courses)