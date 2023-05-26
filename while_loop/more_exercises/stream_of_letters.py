c, o, n = 0, 0, 0
word = ""

while True:
    letter = input()

    if letter == "End":
        break

    if letter == "c" and c == 0:
        c = 1
    elif letter == "o" and o == 0:
        o = 1
    elif letter == "n" and n == 0:
        n = 1
    else:
        if letter.isalpha():
            word += letter

    if c == 1 and o == 1 and n == 1:
        c, o, n = 0, 0, 0
        print(word, end=" ")
        word = ""