class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        word1 = A
        word2 = B
        # DP talbe, i is the position in word1, and j is the position in word2
        distance = [[0 for j in range(len(word2)+1)]
                    for i in range(0, len(word1)+1)]
    # when i or j=0 means empty string, the distance is the length of another string
        for i in range(0, len(distance)):
            for j in range(0, len(distance[0])):
                if (i == 0):
                    distance[i][j] = j
                elif (j == 0):
                    distance[i][j] = i
        # if word1[i] == word2[j], then the distance of i and j is the previous i and j
        # otherwise we either replace, insert or delete a char
        # when insert a char to word1 it means we are trying to match word1 at i-1 to word2 at j
        # when delete a char from word1 it equals to insert a char to word2, which
        # means we are trying to match word1 at i to word2 at j-1
        # when replace a char to word1, then we add one step to previous i and j
        for i in range(1, len(distance)):
            for j in range(1, len(distance[0])):
                if (word1[i - 1] == word2[j - 1]):
                    distance[i][j] = distance[i - 1][j - 1]
                else:
                    distance[i][j] = 1 + min(distance[i - 1][j - 1],
                                             min(distance[i - 1][j], distance[i][j - 1]))

        return distance[len(word1)][len(word2)]


print(Solution().minDistance("b", "a"))
