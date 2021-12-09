# Author MB 12/09/2021

def count_odds(lst):
    total = 0
    for odd in lst:
        if odd % 2 != 0:
            total += 1
            odd += 1
        else:
            odd += 1
    return total

print(count_odds([1, 2, 3, 4, 5, 6]) == 3)
print(count_odds([1, 3, 5, 7, 9]) == 5)
print(count_odds([2, 4, 6, 8, 10]) == 0)