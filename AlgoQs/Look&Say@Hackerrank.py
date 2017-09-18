#Look and Say
import sys

def tonextcount(l):
    next = []
    i = 0
    count = 1
    if len(l) == 1:
        return ["1" + str(l)]
            
    while i < len(l)-1:
        if l[i] == l[i+1]:
            count += 1
            i+= 1
            continue
        else:
            next.append(str(count))
            next.append(str(l[i]))
            count =1
        i += 1
    if count!= 1:
        next.append(str(count))
        next.append(str(l[-1]))
    if l[-1] != l[-2]:
        next.append("1")
        next.append(str(l[-1]))
    return next

for line in sys.stdin:
    input = line
    break
K = input.split()[0]
nums = input.split()[1:]


list= []
for index in range(0,int(K)+1):
    list.append([])
list[0] = nums

index = 1
while index < int(K)+1:
    list[index] = tonextcount(list[index-1])
    index += 1

length = max([len(x) for x in [" ".join(b) for b in list]])

for l in list: 
    if length % 2 == len(" ".join(l))%2 :
        if length == len(" ".join(l)):
            print(" ".join(l))
            continue
        print("." * int( (length-len(" ".join(l) ))/2 ),end="")
        print(" ".join(l),end="")
        print("." * int( (length-len(" ".join(l) ))/2 ))
    else:
        print("." * int( (length+1-len(" ".join(l) ))/2 ),end="")
        print(" ".join(l),end="")
        print("." * int( (length-1-len(" ".join(l) ))/2 ))
print(len(list[-1]))
