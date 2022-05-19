# In the classic problem of the Towers of Hanoi, you have 3 towers numbered from 1 to 3 (left to right) and
# A disks numbered from 1 to A (top to bottom) of different sizes which can slide onto any tower.
# The puzzle starts with disks sorted in ascending order of size from top to bottom
# (i.e., each disk sits on top of an even larger one).

# You have the following constraints:
# Only one disk can be moved at a time.
# A disk is slid off the top of one tower onto another tower.
# A disk cannot be placed on top of a smaller disk.

# You have to find the solution to the Tower of Hanoi problem.
# You have to return a 2D array of dimensions M x 3,
# where M is the minimum number of moves needed to solve the problem.
# In each row, there should be 3 integers (disk, start, end), where:

# disk - number of disk being moved
# start - number of the tower from which the disk is being moved
# stop - number of the tower to which the disk is being moved

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def towerOfHanoi(self, A):
        # ll = (1 << A)  i.e. 2^A
        res = []
        self.toh(A, 1, 3, 2, res)
        return res

    def toh(self, disks, source, destination, aux, res):
        if disks == 0:
            return

        self.toh(disks - 1, source, aux, destination, res)
        res.append([disks, source, destination])
        self.toh(disks-1, aux, destination, source, res)
