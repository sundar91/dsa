maxn = 100009
graph = []
visited = []


def ini():
    global maxn, graph, visited
    graph = [[] for i in range(maxn)]
    visited = [0]*maxn


def isReachable(s, d):
    global graph, visited
    # Mark all the vertices as not visited
    # Create a queue for BFS
    queue = []
    # Mark the source node as visited and enqueue it
    queue.append(s)
    visited[s] = True
    while queue:
        # Dequeue a vertex from queue
        n = queue.pop(0)
        # If this adjacent node is the destination node,
        # then return true
        if n == d:
            return True
        #  Else, continue to do BFS
        for i in graph[n]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    # If BFS is complete without visited d
    return False


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        global visited, maxn, graph
        ini()
        for edge in B:
            graph[edge[0]].append(edge[1])
        if(isReachable(1, A) == True):
            return 1
        return 0
