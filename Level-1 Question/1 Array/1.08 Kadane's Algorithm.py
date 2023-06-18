a1 = input()
a1 = a1.split(",")

b1 = []
for i in a1:
    b1 = b1 + [int(i)]

def  maxSubarraySum(a):
    curr = 0
    max = 0
    for i in a:
        curr += i
        if curr > max:
            max = curr
        if curr < 0:
            curr = 0
    if max == 0:
        a.sort()
        return a[-1]
    return max

print(maxSubarraySum(b1))
