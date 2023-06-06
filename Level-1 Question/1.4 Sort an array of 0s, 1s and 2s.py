a = input()
a = a[1:-1]
a = a.split(',')
b = []
for i in range(len(a)):
    b = b + [int(a[i])]

def sort012(a):
    s0 = []
    s1 = []
    s2 = []

    for i in a:
        if int(i) == 0:
            s0 = s0 + [0]
        #print(s0)
        if int(i) == 1:
            s1 = s1 + [1]
        #print(s1)
        if int(i) == 2:
            s2 = s2 + [2]
        #print(s2)
    l = s0 + s1 + s2
    return l
print(sort012(b))