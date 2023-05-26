text = input()

sum_of_letters = 0

for i in range(0, len(text)):
    if text[i] == "a":
        sum_of_letters += 1
    if text[i] == "e":
        sum_of_letters += 2
    if text[i] == "i":
        sum_of_letters += 3
    if text[i] == "o":
        sum_of_letters += 4
    if text[i] == "u":
        sum_of_letters += 5

print(sum_of_letters)