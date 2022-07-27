
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.child = defaultdict()
        self.end = False


class Solution:
    def __init__(self):
        self.root = TrieNode()
    # @param A : list of strings
    # @param B : list of strings
    # @return a strings

    def solve(self, A, B):
        for i in range(len(A)):
            self.insert(A[i])

        res = []
        for i in range(len(B)):
            d = self.traverse(B[i])
            res.append(d)

        return ''.join(res)

    def search(self, s):
        current = self.root
        for i in range(len(s)):
            if not s[i] in current.child:
                return False
            
            current = current.child[s[i]]
        
        return True


    def traverse(self, s):
        str_list = list(s)

        match_found = False

        for i in range(len(s)):
            # replace the current char index with all 26 characters 
            temp = str_list[i]
            for j in range(ord('a'), ord('z') + 1):
                replace_char = chr(j)
                if replace_char != temp:
                    str_list[i] = replace_char
                    if self.search(str_list) :
                        match_found = True
                        break
            
            if match_found:
                break
            else:
                str_list[i] = temp 
        
        if match_found:
            return '1'
        else:
            return '0'

        
    def insert(self, s):
        current = self.root
        for i in range(len(s)):
            if not s[i] in current.child:
                current.child[s[i]] = TrieNode()

            current = current.child[s[i]]

        current.end = True


print(Solution().solve(["data", "circle", "cricket"],
      ["date", "circel", "crikket", "data", "circl"]))
