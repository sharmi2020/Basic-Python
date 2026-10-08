# count how many times a particular character appears in a string.
def count_character(line, char):
    count = 0

    for i in line:
        if i == char:
            count += 1

    return count


# Count Vowels
def count_vowels(line):
    count = 0

    for i in line:
        if i in "aeiou":
            count += 1

    return count

def count_uppercase(line):
    count=0
    for i in line:
        if i.isupper():
            count+=1
    return count

def count_digits(line):
    count=0
    for i in line:
        if i.isdigit():
            count+=1
    return count

def first_non_repeating(line):
    for i in line:
        count = 0

        for j in line:
            if i == j:
                count += 1

        if count == 1:
            return i

def first_repeated(line):
    for i in line:
        count = 0

        for j in line:
            if i == j:
                count += 1

        if count > 1:
            return i


        
# remove duplicates
def remove_duplicates(line):
    result = ""

    for i in line:
        found = False

        for j in result:
            if i == j:
                found = True

        if not found:
            result = result + i

    return result