for i in range(20):
    if i % 2 == 0:
        print i
    else:
        i += 1

for i in range(20):
    if i % 2 != 0:
        print i
    else:
        i += 1


def div(a, b):
    if a % b == 0 or b % a == 0:
        return True
    else:
        return False

a = int(raw_input())
b = int(raw_input())
div(a, b)