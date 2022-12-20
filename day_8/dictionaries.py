# Day 8

dog= dict()

dog= {"name":"Rocky","color":"golden","breed":"golden retriever","legs":"four","age":"2 years"}

student_dictionary = {
"first_name":"Juan",
"last_name":"García", 
"gender":"M", 
"marital_status":"unmarried", 
"skills":["music"], 
"country":"Spain", 
"city":"Jerez",
"address":"Chapín"
}

print(len(student_dictionary))

print(student_dictionary["skills"])
print(type(student_dictionary["skills"]))

student_dictionary["skills"].append("computing")
student_dictionary["skills"].append("swimming")

keys = student_dictionary.keys()

values = student_dictionary.values()

items = student_dictionary.items()

del student_dictionary['gender']

del student_dictionary

