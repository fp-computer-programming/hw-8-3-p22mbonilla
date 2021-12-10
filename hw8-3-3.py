# Author MB 12/09/2021

def three_letter_words(word):
    total = 0
    y = 0
    while y < len(word):
        if len(word[y]) == 3:
            total += 1
        y += 1
    return total

print(three_letter_words(["cat", "bat", "apple"]) == 2)
print(three_letter_words(["apple", "hippo", "mouse"]) == 0)
print(three_letter_words(["hop", "pop", "bop"]) == 3)