V = int(input())    # pool`s volume
P1 = int(input())   # flow fist pipe for hour
P2 = int(input())   # flow second pipe for hour
H = float(input())   # hours the worker is absent

water_in_pool = (P1 * H) + (P2 * H)
V_percent = water_in_pool / V * 100
P1_percent = P1 * H / water_in_pool * 100
P2_percent = P2 * H / water_in_pool * 100

if water_in_pool > V:
    print(f"For {H} hours the pool overflows with {water_in_pool - V:.2f} liters.")

else:
    print(f"The pool is {V_percent:.2f}% full. Pipe 1: {P1_percent:.2f}%. Pipe 2: {P2_percent:.2f}%.")
