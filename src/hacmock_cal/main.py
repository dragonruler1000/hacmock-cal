from suspention import calc as scalc
from catc import calc as catc
from unitc import calc as unitc

calcs = {
    "1": ("Suspension", scalc),
    "2": ("Cat curve", catc),
    "3": ("Unit converter", unitc)
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
