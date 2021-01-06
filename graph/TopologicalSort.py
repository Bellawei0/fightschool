from collections import deque


def topological_sort(vertices, edges):
    sortedOrder = []
    if vertices <= 0:
        return sortedOrder

     # a. Initialize the graph
    inDegree = {i: 0 for i in range(vertices)}     # count of incoming edges
    adjList = {i: [] for i in range(vertices)}     # adjacency list graph

    # b. Build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        adjList[parent].append(child)  # put the child into it's parent's list
        inDegree[child] += 1           # increment child's inDegree

    # c. Find all sources i.e., all vertices with 0 in-degrees
    queue = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            queue.append(key)

    # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    while queue:
        vertex = queue.popleft()
        sortedOrder.append(vertex)
        # get the node's children to decrement their in-degrees
        for child in adjList[vertex]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                queue.append(child)

    # topological sort is not possible as the graph has a cycle
    if len(sortedOrder) != vertices:
        return []

    return sortedOrder


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))


main()
