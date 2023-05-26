stadium_capacity = int(input())
fans_count = int(input())

a_sector = 0
b_sector = 0
v_sector = 0
g_sector = 0

for num in range(fans_count):
    sector = input()

    if sector == "A":
        a_sector += 1
    elif sector == "B":
        b_sector += 1
    elif sector == "V":
        v_sector += 1
    else:
        g_sector += 1

print(f"{a_sector / fans_count * 100:.2f}%")
print(f"{b_sector / fans_count * 100:.2f}%")
print(f"{v_sector / fans_count * 100:.2f}%")
print(f"{g_sector / fans_count * 100:.2f}%")
print(f"{fans_count / stadium_capacity * 100:.2f}%")