# Author MB 12/09/2021

def sum_odds(lst):
    total = 0
    for x in lst:
        if x % 2 != 0:
            total += x
            x += 1
        else:
            x += 1
    return total

print(sum_odds([1, 2, 3, 4, 5, 6]) == 9)
print(sum_odds([1, 3, 5, 7, 9]) == 25)
print(sum_odds([2, 4, 6, 8, 10]) == 0)