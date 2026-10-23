from utils import ask_number

def calc():
    fbw = ask_number("How much does the fabric weight (osy)", 1.9)
    fbs = ask_number("How many yards of fabric are you using", 10)
    cdw = ask_number("What is the weight of your cord (oz/ft)", 0.32)
    cdl = ask_number("how many feet of cord are you using", 36)
    fb = fbw * fbs
    cd = cdw * cdl
    tw = fb + cd
    print("total weight (oz): " + str(tw))