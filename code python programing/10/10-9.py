import math
import cmath

def safe_sqrt(num):
    try:
        ret = math.sqrt(num)
    except ValueError:
        ret = cmath.sqrt(num)
    return ret


if __name__ == "__main__":
    print safe_sqrt(4)
    print safe_sqrt(-4)