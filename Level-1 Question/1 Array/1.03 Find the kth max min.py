k = int(input())
w = input()
w = w.split(" ") #input string w = ["7","10",......]
l = []
for i in range(len(w)):
    l = l + [int(w[i])] # [7,10,....]





def kthmax(k,l):
    min = l[0]


    for i in range(k-1):


        for i in l:
            if i < min:
                min = i
        #l.pop(max)
        l.pop(int(l.index(min)))
        min = l[0]

        
    for i in l:
        if i < min:
            min = i
    return min
    
print(kthmax(k,l))