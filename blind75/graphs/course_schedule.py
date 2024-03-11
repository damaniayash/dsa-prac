'''
This problem biols down to detecting a cycle in the graph
This problem can be solved using Kahn's algorithm.
    Watch this video, if you dont remember -> https://www.youtube.com/watch?v=cIBFEhD77b4
    this algo is used for topological sort of a graph
    The idea is that find nodes with in degree == 0 i.e nodes with no dependencies/incoming edges.
    remove these nodes and reduce the incoming edges of all the adjacent nodes by 1.
    if any adjacent node's incoming eges become 0, add it to the queue.
    Idea is that by starting at nodes with no dependencies and systematically remoing edges, we unpeel a layer of the graph and can remove the next set of nodes in the next itertion
    We also keep a track of the no of nodes popped from the queue.
    If the no of nodes popped == no of original nodes. Graph has no cycles.
    if this is not the case, that means graph has cycle and we can use this to detect cycle in this problem.
We create a graph
    For each node, we store key = node, its neighbors(adjacent nodes) as value. Basically adjacency list.
We create in_degree array
    For each node, we store how many incoming edges does a node have.
    Have 0 incoming edges means that the node has no dependency so this node can be removed first, can serve as a start point for our topological sort.

For every (course, prequestite) we represent it as child, parent.
    we add parent as key and append child as its adjacent node.
    Increase the in_degree of the child by 1.

We want to add all the nodes that have 0 in_degree
    This serves as a starting point, since these nodes have no dependencies
    Append all 0 in_degree nodes in the queue

while queue
    we pop the node
    index += 1 //keep track of the number of popped nodes. If a graph has no cycles the number of popped nodes will be equal to the number of nodes in the original graph
    loop through each adjacent node:
        reduce the in_degree for each node
        if in_degree[adjacent node] == 0 // this means the node has no incoming edge so it can be deleted/popped
            add the node to queue
if index != numcoures // this means there is a cycle in the graph so we can return false, else return trur.


'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i : [] for i in range(numCourses)}
        in_degree = {i : 0 for i in range(numCourses)}
        queue = deque()

        for child, parent in prerequisites:
            graph[parent].append(child)
            in_degree[child] += 1
        
        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)
        
        index = 0
        while queue:
            node = queue.popleft()
            # keep track of no of pops.
            index += 1
            for adj in graph[node]:
                in_degree[adj] -= 1
                # this node has no incoming edges
                if in_degree[adj] == 0:
                    queue.append(adj)

        if index == numCourses:
            return True
        else:
            return False      



        

