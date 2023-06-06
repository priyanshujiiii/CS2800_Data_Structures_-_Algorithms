def maxmin(a):
    max = a[0]
    min = a[0]
    for i in a:
        if i > max:
            max = i
        if i < min:
            min = i
    return max+min
a = input()
a = a[1:-1]
a = a.split(',')
b = []
for i in range(len(a)):
    b = b + [int(a[i])]
print(maxmin(b))