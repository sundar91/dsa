class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        q = []
        res = []
        for i in range(B):
            if len(q) == 0:
                q.append(int(A[i]))
                continue

            rear = q[-1]
            while rear < int(A[i]):
                q.pop()
                if len(q) == 0:
                    break
                rear = q[-1]

            q.append(int(A[i]))

        res.append(q[0])

        for i in range(1, len(A) - B + 1):
            val = int(A[B + i - 1])
            top = q[0]
            if top == A[i-1]:
                q.pop(0)

            if len(q) > 0:
                rear = q[-1]
                while rear < val:
                    q.pop()
                    if len(q) == 0:
                        break
                    rear = q[-1]

            q.append(val)
            res.append(q[0])

        return res


print(Solution().slidingMaximum(['648', '614', '490', '138', '657', '544', '745', '582', '738', '229', '775', '665', '876', '448', '4', '81', '807', '578', '712', '951', '867', '328', '308',
      '440', '542', '178', '637', '446', '882', '760', '354', '523', '935', '277', '158', '698', '536', '165', '892', '327', '574', '516', '36', '705', '900', '482', '558', '937', '207', '368'], 9))
