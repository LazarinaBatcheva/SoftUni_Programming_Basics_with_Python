world_record_in_sec = float(input())

distance_in_meters = float(input())
time_in_sec_for_one_meter = float(input())

water_resistance = distance_in_meters // 15 * 12.5

total_score = distance_in_meters * time_in_sec_for_one_meter + water_resistance

if total_score < world_record_in_sec:
    print(f"Yes, he succeeded! The new world record is {total_score:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_score - world_record_in_sec:.2f} seconds slower.")
