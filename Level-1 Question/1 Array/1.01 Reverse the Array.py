a = input()
a=a.split(",")
b1 = []
for i in a:
    b1 = b1 + [int(i)]
def reverse(k):
    l = []
    for i in k:
        l = [i] + l
    return l

print(reverse(b1))