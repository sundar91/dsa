class TrieNode:
    def __init__(self):
        self.children = {}
        self.leaf = 0


class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def insert(self, x):
        root = self.root
        for i in range(31, -1, -1):
            index = self.check(x, i)
            if index not in root.children:
                root.children[index] = self.get_node()
            root = root.children.get(index)
        root.leaf = True

    def check(self, x, i):
        if((x & (1 << i)) != 0):
            return True
        else:
            return False

    def findXor(self, x):
        root = self.root
        ans = 0
        for i in range(31, -1, -1):
            f = self.check(x, i)
            index = f ^ 1
            if index not in root.children:
                root = root.children.get(index ^ 1)
            else:
                ans = ans + (1 << i)
                root = root.children.get(index)

        return ans


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        for i in range(1, n):
            A[i] = A[i] ^ A[i-1]
        ans = [1, 1]
        maxx = A[0]
        t = Trie()
        t.insert(A[0])
        mp = {}             # to store the indices of the XOR value
        mp[A[0]] = 0
        for i in range(1, n):
            mp[A[i]] = i
            # Case 1 check for subarray(0, i)
            if(A[i] > maxx):
                maxx = A[i]
                ans[0] = 1
                ans[1] = i+1
            elif(A[i] == maxx):
                if(ans[0] != ans[1]):
                    ans[0] = i+1
                    ans[1] = i+1
            curMaxx = t.findXor(A[i])
            res = curMaxx ^ A[i]
            j = mp[res]
            j += 1
            if(curMaxx > maxx):
                maxx = curMaxx
                ans[0] = j+1
                ans[1] = i+1
            # check for minimum length if current maximum  = maxx.
            elif(curMaxx == maxx):
                curL = i-j+1
                ansL = ans[1] - ans[0] + 1
                if(curL < ansL):
                    ans[0] = j+1
                    ans[1] = i+1
            # insert the xor of the prefix(0, i) into the trie.
            t.insert(A[i])
        return ans


print(Solution().solve([1, 2, 3, 4, 5]))
