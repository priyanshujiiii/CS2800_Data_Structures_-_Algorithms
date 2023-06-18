a1 = input()
a1 = a1.split(",")

b1 = []
for i in a1:
    b1 = b1 + [int(i)]

print([b1[-1]]+b1[0:-1] )