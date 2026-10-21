# buy and sell stock
def buy_sell(prices):
    min_price=prices[0]
    profit=0

    for i in range(1,len(prices)):
        if prices[i]<min_price:
            min_price=prices[i]

        current_profit=prices[i]-min_price

        if current_profit>profit:
            profit=current_profit
    return profit

# contains_dupliates
def contains_duplicates(nums):
    res=[]
    for i in nums:
        if i in res:
            
            return True
        else:
            res.append(i)
    return False

# Move zeroes
def move_zeroes(nums):
    res=[]
    for i in nums:
        if i!=0:
            res.append(i)
    for i in nums:
        if i==0:
            res.append(i)
    return res

#  product of array
def product_except_self(nums):
    res=[]
    for i in range(len(nums)):
         ans=1
         for j in range(len(nums)):
             if i==j:
               continue
             else:
                 ans*=nums[j]
    res.append(ans)          
    return res

# max_subarray
def max_sub_array(nums):
    largest_sum=nums[0]
    for i in range(len(nums)):
         curr_sum=0
         for j in range(i,len(nums)):
            curr_sum+=nums[j]
            if curr_sum>largest_sum:
                largest_sum=curr_sum
    return largest_sum