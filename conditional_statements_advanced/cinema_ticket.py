day_of_week = input()

ticket_price = 0

if day_of_week in ["Monday", "Tuesday", "Friday"]:
    ticket_price = 12

elif day_of_week == "Wednesday" or day_of_week == "Thursday":
    ticket_price = 14

elif day_of_week == "Saturday" or day_of_week == "Sunday":
    ticket_price = 16

print(ticket_price)