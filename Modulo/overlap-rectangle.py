# Eight integers A, B, C, D, E, F, G, and H represent two rectangles in a 2D plane.
# For the first rectangle, its bottom left corner is (A, B), and the top right corner is (C, D), 
# and for the second rectangle, its bottom left corner is (E, F), and the top right corner is (G, H).

# Find and return whether the two rectangles overlap or not.

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @param G : integer
    # @param H : integer
    # @return an integer
    def solve(self, A, B, C, D, E, F, G, H):
        # check if cordinates are above or below 
        if F >= D or H <= B:
            return 0
        # if rectangle to left or right
        if E >= C or G <= A: 
            return 0
        return 1