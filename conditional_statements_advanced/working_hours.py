hour = int(input())
day_of_week = input()

if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] and 10 <= hour <= 18:
    print("open")

else:
    print("closed")