from sys import maxsize

n = int(input())

odd_sum = 0
odd_min = maxsize
odd_max = -maxsize
even_sum = 0
even_min = maxsize
even_max = -maxsize


for num in range(1, n + 1):
    number = float(input())

    if num % 2 != 0:
        odd_sum += number
        if number < odd_min:
            odd_min = number
        if number > even_max:
            odd_max = number

    else:
        even_sum += number
        if number < even_min:
            even_min = number
        if number > even_max:
            even_max = number

print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={odd_min:.2f},") if odd_sum != 0 else print(f"OddMin=No,")
print(f"OddMax={odd_max:.2f},") if odd_sum != 0 else print("OddMax=No,")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={even_min:.2f},") if even_sum != 0 else print(f"EvenMin=No,")
print(f"EvenMax={even_max:.2f}") if even_sum != 0 else print(f"EvenMax=No")