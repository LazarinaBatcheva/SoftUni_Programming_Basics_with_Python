for row in range(1, 8, 2):
    for col in range(1, 8 - row + 1):
        print(" ", end="")
    print("*", end="")

    for col in range(1, row):
        print(" *", end="")
    print()

for row in range(5, 0, -2):
    for col in range(1, row - 8 + 1, -1):
        print(end="" + " ")
    print(end="" + "*")

    for col in range(1, row):
        print(end="" + " " + "*")
    print()

# n = int(input())
#
# for i in range(n):
#     print("   " * (n - i), " * " * (i * 2 + 1))
# for i in range(n - 2, -1, -1):
#     print("   " * (n - i), " * " * (i * 2 + 1))