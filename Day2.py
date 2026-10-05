# mini-max sum
# arr=[1,3,5,7,9]
# def miniMaxSum(arr):
#     total = 0
#     minimum = arr[0]
#     maximum = arr[0]

#     for i in arr:
#         total += i

#         if i > maximum:
#             maximum = i

#         if i < minimum:
#             minimum = i

#     minimum_sum = total - maximum
#     maximum_sum = total - minimum

#     print(minimum_sum, maximum_sum)
           
# def gradingStudents(grades):
#     result = []

#     for i in grades:
#         if i < 38:
#             result.append(i)
#             continue

#         remainder = i % 5
#         difference = 5 - remainder

#         if difference < 3:
#             i += difference

#         result.append(i)

#     return result


# # Counting Valleys
# def countingValleys(steps, path):
#     level = 0
#     count = 0

#     for i in path:
#         if i == "U":
#             level += 1

#             if level == 0:
#                 count += 1

#         elif i == "D":
#             level -= 1

#     return count