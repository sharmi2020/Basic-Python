# two sum
def two_sum(arr,target):
    # res=[]
    for i in range(len(arr)):
        for j in range (i+1,len(arr)):
            if arr[i]+arr[j]==target:
                return i,j
# move_zeros
def move_zeros(arr):
    res=[]
    for i in arr:
        if i!=0:
            res.append(i)
    for i in arr:
        if i==0:
            res.append(i)
    return res

# missing number
def find_missing(arr,n):
    for i in range(1,n+1):
        if i not in arr:
            return i
        
# non-repeating character
def first_unique(s):
     freq={}
     for i in s:
         if i in freq:
             freq[i]+=1
         else:
             freq[i]=1

     for i in s:
         if freq[i]==1:
             return 1

     return None

def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
         mid=(left+right)//2
         if arr[mid]==target:
             return mid
             
         elif target < arr[mid]:
             right = mid-1
         else:
            left = mid+1
    return -1


def binary_search(arr, target):
    left=0
    right=len(arr)-1

    while left<=right:
        mid= (left+right) //2

        if arr[mid]==target:
            return mid
        elif target < arr[mid]:
            right=mid-1
        else:
            left=mid+1
    return -1