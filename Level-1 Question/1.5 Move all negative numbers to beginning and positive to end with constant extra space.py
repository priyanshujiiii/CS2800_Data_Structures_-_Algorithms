a = input()

a = a[1:-1]
a = a.split(',')
b = []
for i in range(len(a)):
    b = b + [int(a[i])]

def posneg(a):
    h = []
    k = []
    for i in a:
        if i > 0:
            h = h + [i]
        else:
            k = k + [i]
    return k + h

print(posneg(b))
