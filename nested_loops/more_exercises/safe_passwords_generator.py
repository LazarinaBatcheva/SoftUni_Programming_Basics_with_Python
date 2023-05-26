number_a = int(input())
number_b = int(input())
max_number_of_passwords = int(input())

combinations_counter = 0
flag = False

for A in range(35, 56):
    for B in range(64, 97):
        for x in range(1, number_a + 1):
            for y in range(1, number_b + 1):

                print(f"{chr(A)}{chr(B)}{str(x)}{str(y)}{chr(B)}{chr(A)}", end="|")

                if x == number_a and y == number_b:
                    flag = True
                    break

                combinations_counter += 1

                if combinations_counter == max_number_of_passwords:
                    flag = True
                    break

                A += 1
                if A > 55:
                    A = 35
                B += 1
                if B > 96:
                    B = 64

            if flag == True:
                break
        if flag == True:
            break
    if flag == True:
        break