student_tickets, standard_tickets, kids_tickets = 0, 0, 0

while True:
    film_name = input()

    if film_name == "Finish":
        break

    capacity_salon = int(input())
    sold_tickets = 0

    while sold_tickets < capacity_salon:
        ticket_type = input()

        if ticket_type == "End":
            break

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        else:
            kids_tickets += 1

        sold_tickets += 1

    print(f"{film_name} - {sold_tickets / capacity_salon * 100:.2f}% full.")

total_tickets = student_tickets + standard_tickets + kids_tickets

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_tickets * 100:.2f}% standard tickets.")
print(f"{kids_tickets / total_tickets * 100:.2f}% kids tickets.")