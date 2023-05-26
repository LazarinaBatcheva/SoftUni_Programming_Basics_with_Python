men = int(input())
women = int(input())
number_of_tables = int(input())

full_tables = 0

for i in range(1, men + 1):
    for j in range(1, women + 1):

        if full_tables == number_of_tables:
            break
        else:
            print(f"({i} <-> {j})", end=" ")

        full_tables += 1