from collections import defaultdict


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E, F):

        g = defaultdict(list)
        for i in range(len(B)):
            g[B[i]].append(C[i])
            g[C[i]].append(B[i])

        levels = defaultdict(list)

        visited = {}

        def findDepth(node, l):

            visited[node] = True
            levels[l].append(D[node - 1])
            max1 = 0
            for u in g[node]:
                if u not in visited:
                    depth = findDepth(u, l + 1)
                    max1 = max(max1, depth + 1)

            return max1

        def binarySearch(x, searchlist):
            s, e = 0, len(searchlist) - 1
            ans = -1
            while s <= e:
                mid = s + (e - s) // 2

                if searchlist[mid] >= x:
                    ans = searchlist[mid]
                    e = mid - 1
                else:
                    s = mid + 1

            return ans

        d = findDepth(1, 0)

        for lv in levels:
            levels[lv].sort()

        res = []

        for i in range(len(E)):
            l = E[i] % (d + 1)
            res.append(binarySearch(F[i], levels[l]))

        return res


print(Solution().solve(5, [1, 4, 3, 1], [5, 2, 4, 4], [
      7, 38, 27, 37, 1], [1, 1, 2], [32, 18, 26]))
