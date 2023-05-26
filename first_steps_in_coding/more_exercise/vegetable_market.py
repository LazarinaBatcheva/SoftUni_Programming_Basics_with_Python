N_lv_kg_vegetables = float(input())
M_lv_kg_fruit = float(input())
vegetables_total_kg = int(input())
fruit_total_kg = int(input())

EURO = 1.94

lv_total_revenues = (N_lv_kg_vegetables * vegetables_total_kg) + (M_lv_kg_fruit * fruit_total_kg)
euro_total_revenues = lv_total_revenues / EURO

print(f"{euro_total_revenues:.2f}")
