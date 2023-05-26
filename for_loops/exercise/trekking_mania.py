groups = int(input())

musalla = 0
mont_blank = 0
kilimanjaro = 0
k2 = 0
everest = 0

for _ in range(groups):
    group_members = int(input())
    if group_members < 6:
        musalla += group_members
    elif group_members < 13:
        mont_blank += group_members
    elif group_members < 26:
        kilimanjaro += group_members
    elif group_members < 41:
        k2 += group_members
    else:
        everest += group_members

total_members = musalla + mont_blank + kilimanjaro + k2 + everest

print(f"{musalla / total_members * 100:.2f}%")
print(f"{mont_blank / total_members * 100:.2f}%")
print(f"{kilimanjaro / total_members * 100:.2f}%")
print(f"{k2 / total_members * 100:.2f}%")
print(f"{everest / total_members * 100:.2f}%")