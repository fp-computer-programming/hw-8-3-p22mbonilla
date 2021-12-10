# Author MB 12/09/2021

def count_odds(num):
    total = 0
    y = 0
    while y < len(num):
        if num[y] % 2 != 0:
            total += 1
            y += 1   
        else:
            y += 1
    return total

print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)
print(count_odds([2, 4, 6, 8, 10]) == 0)