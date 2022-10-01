import heapq


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        mod = int(1e9+7)
        n = len(A)
        cars = []
        for i in range(n):
            cars.append((A[i], B[i]))

        cars.sort(key=lambda x: x[0])

        q = []
        profit, count = cars[0][1], 1
        heapq.heappush(q, (cars[0][1], cars[0][0]))

        i = 1
        while len(q) > 0 and i < n:
            p, d = q[0]

            # if we can schedule it within time
            if cars[i][0] > count:
                heapq.heappush(q, (cars[i][1], cars[i][0]))
                profit += cars[i][1]
                count += 1

            else:
                # if not compare the profit
                if p < cars[i][1]:
                    heapq.heappop(q)
                    profit -= p
                    heapq.heappush(q, (cars[i][1], cars[i][0]))
                    profit += cars[i][1]

            i += 1

        return profit % mod


t = [1, 7, 6, 2, 8, 4, 4, 6, 8, 2]
p = [8, 11, 7, 7, 10, 8, 7, 5, 4, 9]

print(Solution().solve(t, p))
