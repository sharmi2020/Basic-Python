# n=[1, 2, 3, 4, 5, 6]
# def count_Even(n):
#     count=0
#     for i in n:
#        if i%2==0:
#          count+=1
#     print(count) 


# arr=[-2, 5,-1, 4, 0, 3]
# def sumPositive(arr):
#     total=0
#     for i in arr:
#         if i>0:
#             total+=i
#     print(total)

# scores=[2,3,6,6,5]
# def runner_up_score(scores):
#     nums=set(scores)
#     # print(nums)
#     largest=0
#     second=0
#     for i in nums:
#         if i>largest:
#             second=largest
#             largest=i
#         elif i>second:
#             second=i
#     return second