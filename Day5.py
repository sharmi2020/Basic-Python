# string construction
# def stringConstruction(s):
#     unique=set(s)
#     count=0
#     for i in unique:
#       count+=1
#     return count



# camelcase
def camelcase(s):
  count =1 
  for i in s:
    if i.isupper():
      count+=1
  return count

# super reduced string
def superReducedString(s):
    result = []

    for i in s:
        if result and i == result[-1]:
            result.pop()
        else:
            result.append(i)

    if not result:
        return "Empty String"

    return "".join(result)