# reverse a string
def reverse_string(s):
    result=""
    for i in s:
        result=i+result
    return result

# largest number
def find_largest(arr):
    largest=arr[0]
    for i in arr:
        if i>largest:
            largest=i
    return largest

# seond largest
def second_largest(arr):
    largest=arr[0]
    second=arr[0]
    for i in arr:
        if i>largest:
            second=largest
            largest=i

        elif i<largest and i>second:
            second=i
    return second

# remove duplicates
def remove_duplicates(arr):
    res=[]
    for i in arr:
        if i not in res:
            res.append(i)
    return res


# count Vowels
def count_vowels(s):
    count=0
    for i in s:
        if i in "aeiou":
            count=count+1
    return count

# count_frequency
def char_frequency(s):
    frequency = {}
    for i in s:
        if i in frequency:
            frequency[i] = frequency[i] + 1
        else:
            frequency[i] = 1
    return frequency



# smallest number
def find_smallest(arr):
    smallest=arr[0]
    for i in arr:
        if i<smallest:
            smallest=i
    return smallest

def find_Even(arr):
    res=[]
    for i in arr:
        if i%2==0:
            res.append(i)
    return res




