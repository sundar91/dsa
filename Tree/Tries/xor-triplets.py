lg = 20
# Structure of a Trie Node


class TrieNode:
    # Constructor to initialize a newly created node
    def __init__(self):
        self.children = [None, None]
        self.sum_of_indexes = 0
        self.number_of_indexes = 0

# Function to insert curr_xor into the trie


def insert(node, num, index):

    for bits in range(lg, -1, -1):
        # Check if the current bit is set or not
        curr_bit = (num >> bits) & 1

        # If this node isn't already present in the trie structure insert it into the trie.
        if (node.children[curr_bit] == None):
            node.children[curr_bit] = TrieNode()
        node = node.children[curr_bit]

    # Increase the sum of indexes by the current index value
    node.sum_of_indexes += index

    # Increase the number of indexes by 1
    node.number_of_indexes += 1


# Function to check if curr_xor is present in trie or not
def query(node, num, index):
    for bits in range(lg, -1, -1):
        # Check if the current bit s set or not
        curr_bit = (num >> bits) & 1
        # If this node isn't already present in the trie structure that means no sub array till current index has 0 xor so
        # return 0
        if (node.children[curr_bit] == None):
            return 0
        node = node.children[curr_bit]

    # Calculate the number of index inserted at final node
    sz = node.number_of_indexes

    # Calculate the sum of index inserted at final node
    Sum = node.sum_of_indexes
    ans = (sz * index) - (Sum)
    return ans


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        curr_xor = 0
        mod = 1e9+7
        number_of_triplets = 0
        n = len(A)
        # The root of the trie
        root = TrieNode()
        for i in range(n):
            x = A[i]
            # Insert the curr_xor in the trie
            insert(root, curr_xor, i)

            # Update the cumulative xor
            curr_xor ^= x

            # Check if the cumulative xor is present in the trie or not if present then add (sz * index) - sum
            number_of_triplets += query(root, curr_xor, i)
            number_of_triplets %= mod
        return int(number_of_triplets)


print(Solution().solve([5, 2, 7, 9, 1, 8]))
