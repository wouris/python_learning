# tuples = list, which is ordered, but cannot be changed

student = ("pero","21","male")

print(student.count("bro"))
print(student.index("male"))

for i in student:
    print(i)

if "bro" in student:
    print("True")
else:
    print("False")
