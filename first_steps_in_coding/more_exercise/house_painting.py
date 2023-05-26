x = float(input())
y = float(input())
h = float(input())

walls_area = (2 * (x * x + x * y)) - (1.2 * 2 + 2 * (1.5 * 1.5))
roof_area = (2 * (x * y)) + (2 * (x / 2 * h))

green_paint = walls_area / 3.4
red_paint = roof_area / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
