text = "  Hello Python WORLD  "
print(len(text.strip().lower().split()))

text = "Apple and Banana"
print(text.count("a"))

text = "  PYTHON Is FUN  "
print(text.strip().lower())

text = "Python is easy and Python is powerful"
res=text.replace("Python","Java")
print(res.split())
print(len(res.split()))

text = "Python python PYTHON Java Python"
print(text.lower().count("python"))

text = "Python is very interesting"
res=text.split()
print("-".join(res))

text = "Python programming is fun"
res=text.startswith("Python")
print(res)

print(text.find("programming"))

text = "apple mango apple banana apple"
res=text.replace("apple","orange")
print(res)
print(text.count("apple"))

text = "  learn python step by step  "
res=text.strip()
res1=res.split()
print("-".join(res1).upper())

text1 = "Python123"
text2 = "12345"
text3 = "Python"
print(text1.isalpha())
print(text2.isdigit())
print(text3.isalpha())

filename = "report_final.pdf"
res=filename.startswith("report")
res1=filename.endswith(".pdf")
res2=filename.replace("final","draft")
print(res)
print(res1)
print(res2)

text = "python programming is fun"
res=text.capitalize()
res1=text.title()
res2=text.upper()
print(res2)
print(res)

text = "  Python is easy and Python is useful  "
res=text.strip()
res1=res.lower()
res2=res1.replace("easy","powerful")
print(res2)
res3=res2.count("python")
print(res3)


# Count_Vowels
text = "Hello Python"
res=text.lower()
print(res)
def count_Vowels(res):
    count=0
    for i in res:
        if i in "aeiou":
            count+=1
    return count

print(count_Vowels(res))

# reverse a string

text="hello"
def reverse(text):
    return text[::-1]
print(reverse(text))


def palindrome(text):
    res="" 
    for i in text:
        res=i+res
        # return res
    if text== res:
        return True
    else:
        return False
print(palindrome("madam"))

text = "programming"
target = "g"

def count_char(text,target):
    count=0
    for i in text:
        if i in target:
            count+=1
    return count
print(count_char("programming","g"))

text = "programming"
def duplicate(text):
    res=""
    for i in text:
      if i not in res:
        res=res+i
    return res
print(duplicate("programming"))