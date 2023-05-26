from math import floor

tournaments = int(input())
start_points = int(input())

points = 0
num_of_wins = 0

for _ in range(tournaments):
    stage = input()
    if stage == "W":
        num_of_wins += 1
        points += 2000
    elif stage == "F":
        points += 1200
    else:
        points += 720

total_points = start_points + points

print(f"Final points: {total_points}")
print(f"Average points: {floor(points / tournaments)}")
print(f"{num_of_wins / tournaments * 100:.2f}%")
