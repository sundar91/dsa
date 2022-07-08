class Solution:
    def maximumRemovals(self, s, p, removable) -> int:
        def checkSubsequence():
            l1, l2 = 0, 0
            while l1 < len(s) and l2 < len(p):

                if l1 in removed or s[l1] != p[l2]:
                    l1 += 1
                    continue
                l1 += 1
                l2 += 1

            return l2 == len(p)

        l, r = 0, len(removable) - 1
        res = 0
        while l <= r:
            mid = l + ((r - l) // 2)

            removed = set(removable[:mid+1])

            if checkSubsequence():
                res = max(res, mid + 1)
                l = mid + 1
            else:
                r = mid - 1

        return res
