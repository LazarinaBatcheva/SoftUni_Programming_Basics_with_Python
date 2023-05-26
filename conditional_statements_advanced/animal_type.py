animal_name = input()

if animal_name == "dog":
    print("mammal")

elif animal_name in ["crocodile", "tortoise", "snake"]:
    print("reptile")

else:
    print("unknown")