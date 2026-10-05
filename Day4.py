# apple and orange problem
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0

    for i in apples:
        if s <= a + i <= t:
            apple_count += 1

    orange_count = 0

    for i in oranges:
        if s <= b + i <= t:
            orange_count += 1

    return [apple_count, orange_count]


# Between two sets
def getTotalX(a, b):
    count = 0

    for i in range(max(a), min(b) + 1):
        valid = True

        for x in a:
            if i % x != 0:
                valid = False

        for y in b:
            if y % i != 0:
                valid = False

        if valid:
            count += 1

    return count


#2D array
def diagonalDifference(arr):
    total = 0

    for i in range(len(arr)):
        total += arr[i][i]

    second_total = 0

    for i in range(len(arr)):
        second_total += arr[i][len(arr) - 1 - i]

    diff = abs(total - second_total)

    return diff