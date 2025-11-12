student = {
    "name": "sivacharan",
    "age": 21,
    "course": "Computer Science",
    "grade": "A"
}
print(student)
print(student["name"])    
print(student["course"]) 
student["age"] = 22           
student["city"] = "New York"  
print(student)
student.pop("grade")     
student.popitem()         
del student["course"]     
print(student)
for key in student:
    print(key)
for value in student:
    print(value)





