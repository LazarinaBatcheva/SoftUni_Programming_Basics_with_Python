total_moves = int(input())

result = 0
n1, n2, n3, n4, n5, n6 = 0, 0, 0, 0, 0, 0

for move in range(total_moves):
    number = int(input())

    if 0 <= number <= 9:
        n1 += 1
        result += number * 0.20
    elif 10 <= number < 20:
        n2 +=1
        result += number * 0.30
    elif 20 <= number < 30:
        n3 += 1
        result += number * 0.40
    elif 30 <= number < 40:
        n4 += 1
        result += 50
    elif 40 <= number <= 50:
        n5 += 1
        result += 100
    else:
        n6 += 1
        result = result / 2

print(f"{result:.2f}")
print(f"From 0 to 9: {n1 / total_moves * 100:.2f}%")
print(f"From 10 to 19: {n2 / total_moves * 100:.2f}%")
print(f"From 20 to 29: {n3 / total_moves * 100:.2f}%")
print(f"From 30 to 39: {n4 / total_moves * 100:.2f}%")
print(f"From 40 to 50: {n5 / total_moves * 100:.2f}%")
print(f"Invalid numbers: {n6 / total_moves * 100:.2f}%")