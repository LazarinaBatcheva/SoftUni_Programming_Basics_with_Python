start_interval_letter = input()
end_interval_letter = input()
letter = input()

current_letter = ""
combination = ""
combination_counter = 0

for ch1 in range(ord(start_interval_letter), ord(end_interval_letter) + 1):
    for ch2 in range(ord(start_interval_letter), ord(end_interval_letter) + 1):
        for ch3 in range(ord(start_interval_letter), ord(end_interval_letter) + 1):

            combination = chr(ch1) + chr(ch2) + chr(ch3)

            if letter in combination:
                continue

            combination_counter += 1
            print(combination, end=" ")

print(combination_counter)