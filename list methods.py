marks = [75, 90, 60, 75, 85, 90, 40]
marks.append(95)
marks.remove(75)
print(marks.count(90))
marks.pop(2)
marks.sort()
marks.reverse()
print(marks)

numbers = [10, 20, 10, 40, 30, 20]
numbers.append(50)
numbers.remove(10)
numbers.pop(2)
numbers.sort()
numbers.reverse()
print(numbers)

items = ["milk", "bread", "eggs", "bread"]
items.append("butter")
items.remove("bread")
print(items.count("bread"))
items.pop(1)
items.sort()
items.reverse()
# print(items)

# remove duplicates
nums=[1,2,2,3,1,4]
def remove_duplicates(nums):
    res=[]
    for i in nums:
        if i not in res:
            res.append(i)
    return res

# add negative
nums = [-2, 3, -5, 7, 0, -1, 4]
def add(nums):
  res=[]
  for i in nums:
    if i>=0:
      res.append(i)
  return res

# remove zeros
nums = [0, 4, 0, 2, 7, 0, 3]
def remove_zeros(num):
    res=[]
    for i in nums:
        if i!=0:
            res.append(i)
    return res

nums = [-2, 5, -7, 3, 0, -1, 8]
def positive(nums):
    res=[]
    for i in nums:
        if i>=0:
            res.append(i)
    return res
print(positive(nums))
