deposit_amount = float(input())
term_of_deposit = int(input())
yearly_interest_rate = float(input()) / 100

sum_of_deposit = deposit_amount + term_of_deposit * (deposit_amount * yearly_interest_rate) / 12

print(sum_of_deposit)
