coins_1_lv = int(input())
coins_2_lv = int(input())
banknotes_5_lv = int(input())
amount = int(input())

coins_1_lv_counter = 0
coins_2_lv_counter = 0
banknotes_5_lv_counter = 0

for a in range(0, coins_1_lv + 1):
    for b in range(0, coins_2_lv + 1):
        for c in range(0, banknotes_5_lv + 1):

            total_sum = a + b * 2 + c * 5

            if total_sum == amount:
                print(f"{a} * 1 lv. + {b} * 2 lv. + {c} * 5 lv. = {total_sum} lv.")