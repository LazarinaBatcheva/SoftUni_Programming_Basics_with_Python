juniors_count = int(input())
seniors_count = int(input())
rout = input()

juniors_price = 0
seniors_price = 0

total_counts = juniors_count + seniors_count

if rout == "trail":
    juniors_price = 5.50
    seniors_price = 7
elif rout == "cross-country":
    juniors_price = 8
    seniors_price = 9.50
    if total_counts >= 50:
        juniors_price *= 0.75
        seniors_price *= 0.75
elif rout == "downhill":
    juniors_price = 12.25
    seniors_price = 13.75
else:
    juniors_price = 20
    seniors_price = 21.50

total_price = ((juniors_count * juniors_price) + (seniors_count * seniors_price)) * 0.95

print(f"{total_price:.2f}")