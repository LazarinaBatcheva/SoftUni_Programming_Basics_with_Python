import string

n = int(input())
l = int(input())

alphabet_string_low = string.ascii_lowercase
alphabet_list_lower = list(alphabet_string_low)
l_letters = alphabet_list_lower[:l]

for symbol1 in range(1, n):
    for symbol2 in range(1, n + 2):
        for l in l_letters:
            for symbol4 in l_letters:
                for symbol5 in range(1, n + 3):
                    if symbol1 < symbol5 and symbol5 > symbol2 and symbol5 <= n:
                        print(f"{symbol1}{symbol2}{l}{symbol4}{symbol5}", end=" ")