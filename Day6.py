# Making Anagrams
def makingAnagrams(s1, s2):
    count = 0
    s2 = list(s2)

    for i in s1:
        if i in s2:
            s2.remove(i)
        else:
            count += 1

    count += len(s2)

    return count

# Two strings
def twoStrings(s1, s2):
    for i in s1:
        if i in s2:
            return "YES"

    return "NO"

# Find Largest
def findMax(numbers):
    largest = numbers[0]

    for i in numbers:
        if i > largest:
            largest = i

    return largest

# sum of all numbers
def findSum(numbers):
    total = 0

    for i in numbers:
        total += i

    return total