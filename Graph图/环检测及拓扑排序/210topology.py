from collections import defaultdict
from typing import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegree = [0] * numCourses

        # Create graph and compute in-degrees
        for course, pre in prerequisites:
            adj_list[pre].append(course)
            indegree[course] += 1

        # Add zero in-degree courses to queue
        queue = deque([course for course in range(numCourses) if indegree[course] == 0])
        topological_order = []

        while queue:
            course = queue.popleft()
            topological_order.append(course)
            print('topological_order',topological_order)
            for next_course in adj_list[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    print(next_course)
                    queue.append(next_course)

        return topological_order if len(topological_order) == numCourses else []