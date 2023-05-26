km_counts = int(input())
time_of_trip = str(input())     # day or night

taxi_day_trip_price = 0.70 + km_counts * 0.79       # for < 20 km
taxi_night_trip_price = 0.70 + km_counts * 0.90     # for < 20 km
BUS_PRICE_FOR_ONE_KM = 0.09                         # for >= 20 km
TRAIN_PRICE_FOR_KM = 0.06                           # for >= 100 km

bus_trip_price = km_counts * BUS_PRICE_FOR_ONE_KM
train_trip_price = km_counts * TRAIN_PRICE_FOR_KM
difference_between_bus_and_train_price = bus_trip_price - train_trip_price

if km_counts < 20 and time_of_trip == "day":
    print(f"{taxi_day_trip_price:.2f}")
elif km_counts < 20 and time_of_trip == "night":
    print(f"{taxi_night_trip_price:.2f}")
elif 20 <= km_counts < 100 and difference_between_bus_and_train_price > 0:
    print(f"{bus_trip_price:.2f}")
else:
    print(f"{abs(train_trip_price):.2f}")

