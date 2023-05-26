actor_name = input()
academy_points = float(input())
judges_count = int(input())

min_points = 1250.5
points = 0
total_points = 0

for _ in range(1, judges_count + 1):
    judges_count = len(input())
    judges_points = float(input())

    points += judges_count * judges_points / 2
    total_points = points + academy_points

    if total_points > min_points:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break

else:
    print(f"Sorry, {actor_name} you need {min_points - total_points:.1f} more!")