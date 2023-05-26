yearly_basketball_training_fee = int(input())

sneakers_price = yearly_basketball_training_fee - (yearly_basketball_training_fee * 0.40)
equipment_price = sneakers_price - (sneakers_price * 0.20)
ball_price = equipment_price / 4
accessories_price = ball_price / 5

total_costs = (yearly_basketball_training_fee + sneakers_price + equipment_price + ball_price + accessories_price)

print(total_costs)