student = {
    "name": "Ravi",
    "age": 22,
    "course": "Python"
}
print(student["age"])

student = {
    "name": "Ravi",
    "age": 22,
    "course": "Python"
}
# print(student.get("values"))
# print(student.values())
# print(student.keys())
# print(student.items())
# student.update({"age":23})
# student.pop("course")
x=student.setdefault("city","chennai")
print(x)
print(student)


items = ["apple", "banana", "apple", "orange", "banana", "apple"]
freq={}
for i in items:
    freq[i]=freq.get(i,0)+1
print(freq)
