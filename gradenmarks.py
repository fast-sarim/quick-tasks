student = {
    "name" : input("enter name of student :"),
    "class" : input("enter class of student :"),
    "roll" : input("enter roll of student :"),
    "age" : input("enter age of student :"),
    "gender" : input("enter gender of student :"),
    "subjects" : {
        "math" : input("enter marks of math :"),
        "science" : input("enter marks of science :"),
        "english" : input("enter marks of english :"),
        "social studies" : input("enter marks of social studies :"),              
        "g.k" : input("enter marks of g.k :")
    } 
}
print(student["subjects"]["math"])
print(student["subjects"]["science"])
print(student["subjects"]["english"])
print(student["subjects"]["social studies"])
print(student["subjects"]["g.k"])
print("name of student is :",student[ "name"])
print("class of student is :",student[ "class"])
print("roll of student is :",student[ "roll"])
print("age of student is :",student[ "age"])
print("gender of student is :",student[ "gender"])
print("marks of math is :",student[ "subjects"]["math"])
print("marks of science is :",student[ "subjects"]["science"])
print("marks of english is :",student[ "subjects"]["english"])
print("marks of social studies is :",student[ "subjects"]["social studies"])
print("marks of g.k is :",student[ "subjects"]["g.k"])

