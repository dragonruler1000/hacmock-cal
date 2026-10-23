from suspention import calc as scalc
from catc import calc as catc
from unitc import calc as unitc
from tarpsize import calc as tarps
from weightc import calc as wc

calcs = {
    "1": ("Suspension", scalc),
    "2": ("Cat curve", catc),
    "3": ("Unit converter", unitc),
    "4": ("tarp size", tarps),
    "5": ("hammock weight", wc)
}
print("Hammock calculator")
print("A calculator for most of your hammock needs")
print()

loop = 1

while loop >= 1:
    print()
    print("advalible calculators:")
    for key, (name, _) in calcs.items():
        print(f"{key}: {name}")


    choice = input("What calculator do you want to use or q to quit: ")
    if choice in calcs:
        name, func = calcs[choice]
        print("loading " + name)
        print(func())
    elif choice == "q":
        loop= 0
    else:
        print("invalid choice")
