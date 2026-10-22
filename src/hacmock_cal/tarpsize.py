from utils import ask_number
import math

def tarp_size(hammock_len, hammock_width, pitch_deg, side_overhang=12, end_overhang=12):
    # all legths are in inches
    reach = hammock_width / 2 + side_overhang
    slope  = reach / math.cos(math.radians(pitch_deg))
    width = 2 * slope
    length = hammock_len + 2 * end_overhang
    edge_drop = reach * math.tan(math.radians(pitch_deg)) # edge height below ridge
    print("width = " + str(width) + " length = " + str(length) + " edge drop = " + str(edge_drop))

def stake_distance(edge_height, cord_length):
    return math.sqrt(cord_length**2 + edge_height**2)

def calc():
    hammock_len = ask_number("how long is your hammock", 76)
    hammock_width = ask_number("How wide is your hammock", 50)
    pitch_deg = ask_number("What angle do you want your tarp to be at", 30)
    print(tarp_size(hammock_len, hammock_width, pitch_deg))
    edge_height = ask_number("How high off the ground is the edge of your tarp (inches)", 36)
    cord_length = ask_number("How long is your cord holding your tarp (inches?", 12)
    print(round(stake_distance(edge_height, cord_length), 2))