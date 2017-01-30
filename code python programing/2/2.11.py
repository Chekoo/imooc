# coding : gbk
# set a dict
d = {1: "sum",
     2: "avg",
     3: "output",
     4: "quit"
    }

for a, b in d.items():
    print a, b

# input five number

print "Please enter five number"
l = []
for i in range(5):
    num = int(raw_input())
    l.append(num)

print l

def prod(x, y):
    return x * y

while 1:
    p = int(raw_input())
    if p == 1:
        print  "sum: ",sum(l)
    elif p == 2:
        print  "average: ", sum(l) / 5
    elif p == 3:
        print "product: ", reduce(prod, l)
    elif p == 4:
        print "Quit! Bye Bye!"
    else:
        print "The choice is not ok!"