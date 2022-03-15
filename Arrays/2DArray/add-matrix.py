def solve(A, B):
     n = len(A)
     m = len(B)
     C = []
     for i in range(0, n):
        C.append([0] * m)
        for j in range(0, m):
            print(A[i][j])
     return C


A1 =  [[6],[2],[3],[10],[1],[3]]
B1 =  [
  [6],
  [7],
  [3],
  [8],
  [1],
  [2]
]

print(solve(A1, B1))