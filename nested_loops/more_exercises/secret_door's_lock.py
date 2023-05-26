hundreds_limit = int(input())
tens_limit = int(input())
units_limit = int(input())

for hundreds in range(1, hundreds_limit + 1):
    if hundreds % 2 == 0:
        for tens in range(1, tens_limit + 1):
            if str(tens) in '2357':
                for units in range(1, units_limit + 1):
                    if units % 2 == 0:
                        print(hundreds, tens, units)