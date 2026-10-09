# Second Largest
def second_largest(nums):
   largest = 0
   second = 0

   for i in nums:
       if i > largest:
        second = largest
        largest = i
       elif i > second:
        second = i
        return second

# move zeroes to end
def move_zeros(nums):
    res = []

    for i in nums:
        if i != 0:
            res.append(i)

    for i in nums:
        if i == 0:
            res.append(i)

    return res

print(move_zeros([0, 1, 0, 3, 12]))






# Count even numbers
def count_even(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    return count