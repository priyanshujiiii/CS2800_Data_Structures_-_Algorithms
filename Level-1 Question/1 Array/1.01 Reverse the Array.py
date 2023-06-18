a = input()

def reverse(k):
    l = ""
    for i in k:
        l = i + l
    return l

print(reverse(a))