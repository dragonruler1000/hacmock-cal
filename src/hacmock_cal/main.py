from suspention import calc as scalc

calcs = {
    "1": ("Suspension", scalc)
}
print("Hammock calculator")
print("A calculator for most of your hammock needs")
print()
print()
print("advalible calculators:")
for key, (name, _) in calcs.items():
    print(f"{key}: {name}")

choice = input("What calculator do you want to use: ")
if choice in calcs:
    name, func = calcs[choice]
    print("loading " + name)
    print(func())
else:
    print("invalid choice")
