a1 = input()
a1 = a1.split(",")

b1 = []
for i in a1:
    b1 = b1 + [int(i)]


def minJumps(a1):
    a = len(a1)
    b = 0
    c = 0
    for i in range(a):
        b += a1[b]
        c += 1
        if b > a:
            break
        if b ==a:
            break
    return c
print(minJumps(b1))