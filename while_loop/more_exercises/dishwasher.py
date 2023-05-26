detergent = int(input()) * 750

dishes_counter = 0
pots_counter = 0
total_used_detergent = 0
loading_counter = 0

while detergent >= total_used_detergent:
    utensils = input()

    if utensils == "End":
        print(f"Detergent was enough!")
        print(f"{dishes_counter} dishes and {pots_counter} pots were washed.")
        print(f"Leftover detergent {detergent - total_used_detergent} ml.")
        break

    else:
        utensils = int(utensils)
        loading_counter += 1
        if loading_counter % 3 == 0:
            pots_counter += utensils
        else:
            dishes_counter += utensils

    total_used_detergent = (pots_counter * 15) + (dishes_counter * 5)

if total_used_detergent > detergent:
    print(f"Not enough detergent, {total_used_detergent - detergent} ml. more necessary!")