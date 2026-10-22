from utils import ask_number

def mm2in():
    mm = ask_number("mm: ", 25.4)
    inches = mm * 0.0393700787
    print(inches)

def cm2in():
    cm = ask_number("mm: ", 2.54)
    inches = cm * 0.3937007874
    print(inches)

def in2mm():
    inches = ask_number("inches: ", 1)
    mm = inches * 25.4
    print(mm)    

def in2cm():
    inches = ask_number("inches: ", 1)
    cm = inches * 2.54
    print(cm)

def g2oz():
    grams = ask_number("grams: ", 28.349523125)
    oz = grams * 0.0352739619
    print(oz)

def oz2g():
    oz = ask_number("ounces: ", 0.0352739619)
    grams = oz * 28.349523125
    print(grams)

def denier2tex():
    d = ask_number("denier: ", 9)
    t = d/9
    print(t)

def tex2denier():
    t = ask_number("tex: ", 1)
    d = t*9
    print(d)

def denier2dtex():
    d = ask_number("denier: ", 1.11)
    dt = d *10/9
    print(dt)

def dtex2denier():
    dt = ask_number("dtex: ", 0.9)
    d = dt * 9/10

GSM_PER_OSY = 33.9057 # 1 oz/yd² = 33.9057 g/m²

def gsm2osy():
    gsm = ask_number("GSM: ", 33.9057)
    osy = gsm / GSM_PER_OSY
    print(osy)

def osy2gsm():
    osy = ask_number("OSY: ", 1)
    gsm = osy * GSM_PER_OSY
    print(gsm)


converts = {
    "1": ("Milimeters to inches", mm2in),
    "2": ("Centimeters to inches", cm2in),
    "3": ("Inches to centimeters", in2mm),
    "4": ("Inches to centimeters", in2cm),
    "5": ("Grams to Ounces", g2oz),
    "6": ("Ounces to Grams", oz2g),
    "7": ("Denier to Tex", denier2tex),
    "8": ("Tex 2 Denier", tex2denier),
    "9": ("Denier to Dtex", denier2dtex),
    "10": ("Dtex to Denier", dtex2denier),
    "11": ("GSM to OSY", gsm2osy),
    "12": ("OSY to GSM", osy2gsm)
}

def calc():
    print("Conversions:")
    for key, (name, _) in converts.items():
        print(f"{key}: {name}")
    choice = input("What units do you want to convert: ")
    if choice in converts:
        name, func = converts[choice]
        print(func())
