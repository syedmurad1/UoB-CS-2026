# # Older Formatting Methods
# print("Name: {}, Age: {}".format(name, age)) # placeholder -{}


# Using f-strings (Python 3.6+)
# Simplifies string formatting by embedding expressions in {}

name = "Tom"
age = 20
print(f"Name: {name}, Age: {age}")
print(f"Name: {name.upper}, Age: {age}")



student={"id":[1,2],"name": ["Tom","Jerry"], "age": [20,22]}
print(f"ID: {student['id'][0]}, Name: {student['name'][0]}, Age: {student['age'][0]}")
print(f"ID: {student['id'][1]}, Name: {student['name'][1]}, Age: {student['age'][1]}")

#print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")

# for i in range(len(student["id"])):
#     print(f"ID: {student['id'][i]}, Name: {student['name'][i]}, Age: {student['age'][i]}")# print("Name: %s, Age: %d" % (name, age)) # placeholder -%s, %d
# # print("Name: %s, Age: %d" % (name, age)) # placeholder -%s, %d    
