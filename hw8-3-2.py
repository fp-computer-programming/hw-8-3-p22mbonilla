# Author MB 12/09/2021

def sum_odds(num):
    total = 0
    y = 0
    while y < len(num):
        if num[y] % 2 != 0:
            total += num[y]
        y += 1
    return total

print(sum_odds([1, 2, 3, 4, 5, 6]) == 9)
print(sum_odds([1, 3, 5, 7, 9]) == 25)
print(sum_odds([2, 4, 6, 8, 10]) == 0)