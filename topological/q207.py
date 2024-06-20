from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edge = defaultdict(list)
        inbound = [0] * numCourses  # to store the degree of each points, i.e., how many pre requiste for this node
        for x, y in prerequisites:  # y is the pre, x is the result
            inbound[x] += 1
            edge[y].append(x)
        
        q = [i for i in range(numCourses) if inbound[i] == 0]  # get the points that no pre requiste, or we already visit
        visited = 0 # to store the number of points we already visited
        orders = [] # to store
        while q:
            cur = q.pop() # find the 0pre points in order
            visited += 1
            orders.append(cur)
            for n in edge[cur]: # find the current points aftercourse
                inbound[n] -=1
                if inbound[n] == 0:
                    q.append(n)
        return visited == numCourses

