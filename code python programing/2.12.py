print "please enter three numbers: "
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

if a > b:
    num1 = a
    num2 = b
else:
    num1 = b
    num2 = a

if c > num2 and c < num1:
    num3 = num2
    num2 = c
elif c > num1:
    num3 = num2
    num2 = num1
    num1 = c
else:
    num3 = c

print num3, num2, num1