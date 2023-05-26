floors = int(input())
flats = int(input())

flat_name = ""
flat_number = 0

for current_floor in range(floors, 0, -1):
    for number in range(flats):
        apartment_number = current_floor * 10 + number
        if current_floor == floors:
            flat_name = f"L{current_floor}{number}"
        elif current_floor % 2 == 0:
            flat_name = f"O{current_floor}{number}"
        elif current_floor % 2 != 0:
            flat_name = f"A{current_floor}{number}"

        print(flat_name, end=" ")
    print()