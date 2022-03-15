# // ********
# // ***  ***
# // **    **
# // *      *
# // *      *
# // **    **
# // ***  ***
# // ********


# // 1 2 3 4 5 6 7 8 
# // 1 2 3     6 7 8
# // 1 2         7 8
# // 1             8
# // 1 2         7 8
# // 1 2 3     6 7 8
# // 1 2 3 4 5 6 7 8 

def printStar():
    n = int(input())
    m = n * 2
    for i in range(0, n):
        k = n - i -1
        l = n + i
        st = ''
        for j in range(0, m):
            if j <= k or j >= l:
                st += '*'
            else:
                st += ' '
        print(st)
    
    for i in range(0, n):
        k =  i
        l = m - i -1
        st = ''
        for j in range(0, m):
            if j <= k or j >= l:
                st += '*'
            else:
                st += ' '
        print(st)

printStar()