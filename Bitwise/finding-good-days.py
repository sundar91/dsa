# Alex has a cat named Boomer. He decides to put his cat to the test for eternity.

# He starts on day 1 with a stash of food unit, every next day, the stash doubles.

# If Boomer is well behaved during a particular day, she receives food worth equal to the stash on that day.

# Boomer receives a net worth of A units of food. What is the number of days he was well behaved?

def solve(A):
    count  = 0
    while A > 0:
        if A & 1:
            count += 1
        A = A >> 1
    return count

print(solve(5))


def countSetBits(n): 
    # base case 
    if (n == 0): 
        return 0
    else: 
        # if last bit set add 1 else 
        # add 0 
        return (n & 1) + countSetBits(n >> 1)

#  To eat a total of 5 units of food, Boomer behaved normally on Day 1 and on the Day 3.