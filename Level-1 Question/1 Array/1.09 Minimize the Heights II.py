a2 = int(input())
a1 = input()
a1 = a1.split(",")

b1 = []
for i in a1:
    b1 = b1 + [int(i)]

def getMinDiff(a,k):
    l = (a[-1]-k)-(a[0]+k)
    return l

print(getMinDiff(b1,a2))