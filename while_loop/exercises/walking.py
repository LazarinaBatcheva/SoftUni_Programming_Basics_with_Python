steps = input()

TARGET = 10_000
steps_counter = 0

while steps != "Going home":
    steps_counter += int(steps)
    if steps_counter >= TARGET:
        print(f"Goal reached! Good job!\n{steps_counter - TARGET} steps over the goal!")
        break
    steps = input()

if steps == "Going home":
    steps = input()
    steps_counter += int(steps)
    if steps_counter >= TARGET:
        print(f"Goal reached! Good job!\n{steps_counter - TARGET} steps over the goal!")
    else:
        print(f"{TARGET - steps_counter} more steps to reach goal.")