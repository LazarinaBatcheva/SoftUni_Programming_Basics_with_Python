last_sector = input()
rows_in_first_sector = int(input())
seats_of_odd_row = int(input())

all_seats = 0

for sector in range(ord("A"), ord(last_sector) + 1):
    for row in range(1, rows_in_first_sector + 1):
        if row % 2 != 0:
            for seats in range(ord("a"), (ord("a") + seats_of_odd_row)):
                print(f"{chr(sector)}{row}{chr(seats)}")
                all_seats += 1

        elif row % 2 == 0:
            for seats in range(ord("a"), (ord("a") + seats_of_odd_row + 2)):
                print(f"{chr(sector)}{row}{chr(seats)}")
                all_seats += 1

    rows_in_first_sector += 1

print(all_seats)
