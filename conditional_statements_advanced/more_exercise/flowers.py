chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
holiday = input()       # Y - yes, N - no

ARRANGEMENT = 2

flowers = chrysanthemums_count + roses_count + tulips_count

chrysanthemum_price = 0
rose_price = 0
tulip_price = 0

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    rose_price = 4.10
    tulip_price = 2.50
else:
    chrysanthemum_price = 3.75
    rose_price = 4.50
    tulip_price = 4.15

bouquet_price = (chrysanthemums_count * chrysanthemum_price) + \
                (roses_count * rose_price) + \
                (tulips_count * tulip_price)

if holiday == "Y":
    bouquet_price *= 1.15

if flowers > 20:
    bouquet_price *= 0.80

if tulips_count > 7 and season == "Spring":
    bouquet_price *= 0.95

if roses_count >= 10 and season == "Winter":
    bouquet_price *= 0.90

total_price = bouquet_price + ARRANGEMENT

print(f"{total_price:.2f}")
