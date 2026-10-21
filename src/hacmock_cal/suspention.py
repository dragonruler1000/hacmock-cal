import math
from utils import ask_number

def calc():
    distance_ft = ask_number("Distane Between Anchors in feet. default = 14", 14)
    hang_height_in = ask_number("Preferred Sit Height in inches. default = 18", 18)
    weight_lb = ask_number("Weight in Hammock in lbs. default = 175", 175)
    hang_angle_deg = ask_number("Angle in degrees between the suspension cord and the ground. enter angle between 10 to 60 degrees default = 30", 30)
    ridgeline_len_ft = ask_number("Ridge line length in feet. default = 9", 9)
    theta = math.radians(hang_angle_deg)
    ancor_height_ft = round((hang_height_in + (distance_ft * 12/2) * math.tan(theta))/12, 2)
    suspension_len = round(((distance_ft - ridgeline_len_ft) *12)/(2*math.cos(theta)), 1)
    cord_tension = round(weight_lb / (2* math.sin(theta)), 0)
    shear_force = round(cord_tension * math.cos(theta), 1)
    vert_lift = round(cord_tension*math.sin(theta), 1)
    hammock_len = round(ridgeline_len_ft/0.83, 2)
    print("anchor height in ft: " + str(ancor_height_ft))
    print("Suspention length in in: " + str(suspension_len))
    print("Cord Tension in lbs: " + str(cord_tension))
    print("Shear Force in lbs: " + str(shear_force))
    print("Vertical Lift in lbs: " + str(vert_lift))
    print("Hammock Length in ft: " + str(hammock_len))
