import math
from utils import ask_number_int as ask_number
import matplotlib.pyplot as plt

def caternary_params(span, depth):
    #Return (a, arc_length) for a catenary with the given span and sag
    def f(a):
        return a* (math.cosh(span / (2*a)) -1 ) - depth

    # f decreases as a grows, so bracket the toot and bisect
    lo = span / 1400 # keeps cosh from overflowing
    hi = span
    while f(hi) > 0:
        hi *= 2

    for _ in range(100):
        mid = (lo+hi)/2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid

    a = (lo+hi) / 2
    arc_length = 2 * a * math.sinh(span / (2 *a))
    return a, arc_length

def catenary_y(x,a):
    # Height above the lowest point at horizontal offset x from center.
    return a * (math.cosh(x/a) - 1)

def print_table(points):
    print(f"{'x':>8} {'y':>8}")
    for x, y in points:
        print(f"{x:8.3f} {y:8.3f}")

def plot_curve(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    plt.plot(xs, ys, marker="o")
    plt.gca().set_aspect("equal") # Keeps the shape true to scale
    plt.xlabel("x (distance from center)")
    plt.ylabel("y (height above lowest point)")
    plt.title("Catenary curve")
    plt.grid(True)
    plt.show()

def calc():
    cspan = ask_number("What is the span of the curve in in", 60)
    cdepth = ask_number("What is the depth of the curve in in", 6)

    a, arc_length = caternary_params(cspan, cdepth)

    n = int(cspan)
    points = []
    for i in range(n+1):
        x = -cspan / 2 +cspan * i / n
        points.append((x, catenary_y(x, a)))

    print(f"\n Arc length: {arc_length:.3f}")

    mode = input("Output (t = table, p = plot, b = both) [t]: )").strip().lower() or "t"
    if mode in ("t", "b"):
        plot_curve(points)
    if mode in ("p", "b"):
        print_table(points)
    return points
