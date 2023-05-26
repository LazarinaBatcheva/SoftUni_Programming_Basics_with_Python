mackerel_kg_price = float(input()) #skumriq
sprat_kg_price = float(input()) #caca
bonito_kg = float(input()) #palamud
horse_mackerel_kg = float(input()) #safrid
mussels_kg = int(input()) #midi

bonito_price_kg = mackerel_kg_price + mackerel_kg_price * 0.6
horse_mackerel_price_kg = sprat_kg_price + sprat_kg_price * 0.8
mussels_price_kg = 7.50

total_price = \
    (bonito_kg * bonito_price_kg) + \
    (horse_mackerel_kg * horse_mackerel_price_kg) + \
    (mussels_kg * mussels_price_kg)

print(f"{total_price:.2f}")
