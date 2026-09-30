# solve me first

def sum(a,b):
    return a+b
print(sum(3,2))

# sum of its elements
def simpleArraySum(arr):
    sum=0
    for i in arr:
        sum=sum+i
    return sum

# compareTriplets
def compareTriplets(a,b):
    alice_score=0
    bob_score=0
    for i in range():
     if a[0]>b[0]:
        alice_score+=1
     elif a[0]<b[0]:
        bob_score+=1
    return[alice_score,bob_score]

def diagonalDifference(arr):
    left=0
    right=0
    for i in range(3):
        left+=arr[i][i]
        right+=arr[i][2-i]
    return abs(left-right)



candles = [3, 2, 1, 3] 

def birthdayCandles(candles):
    count=0
    for i in candles:
        if i==max(candles):
            count+=1
    return count
print(birthdayCandles([3, 2, 1, 3]))

