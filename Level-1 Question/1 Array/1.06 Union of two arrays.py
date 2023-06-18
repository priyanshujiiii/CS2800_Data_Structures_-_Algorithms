a1 = input()
a2 = input()

a1 = a1.split(" ")
a2 = a2.split(" ")

b1 = []
for i in a1:
    b1 = b1 + [int(i)]
b2 = []
for i in a2:
    b2 = b2 + [int(i)]

def list(b1,b2): 
    a = set()
    for i in b1:
        a.add(i)
    for i in b2:
        a.add(i)
    return len(a)

print(list(b1,b2))

