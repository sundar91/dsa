def bulbs(A):
    switch = 0
    for i in range(0, len(A)):
        temp = switch % 2
        if temp == 0 and A[i] == 0:
            switch += 1
        if temp == 1 and A[i] == 1 :
            switch +=1
    return switch

print(bulbs([1,1,0,0,0,1,0,1,1,1,1,1,1,1,1])) # 4
print(bulbs([1,1,1,1])) # 0
print(bulbs([0,1,0,1])) # 4