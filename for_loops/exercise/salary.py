tabs_count = int(input())
salary = int(input())

fine = 0

for num in range(1, tabs_count + 1):
    site = input()
    if site == "Facebook":
        fine += 150
    elif site == "Instagram":
        fine += 100
    elif site == "Reddit":
        fine += 50

    if salary <= fine:
        print("You have lost your salary.")
        break

else:
    print(f"{salary - fine:.0f}")