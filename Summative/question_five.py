""" Forming adjacency matrix from the input """
def formGraph(n, edges):
    graph = [[0 for i in range(n)] for i in range(n)]

    for i in range(len(edges)):
        graph[edges[i][0]-1][edges[i][1]-1] = edges[i][2]
        graph[edges[i][1]-1][edges[i][0]-1] = edges[i][2]

    return graph

""" Function ShortestReach to find the shortest path from node source to all the vertices """
def shortestReach(n, edges, s):
    # Dikjstra Algorithm 
    graph = formGraph(n, edges)

     # To keep track of vertices that are already been visited and included in MST
    visitedNode = [False] * n
    # To store the key value of the vertices
    # All the keys have been initialized to INFINITY only the 6th vertex to 0
    key = [float('inf')] * n
    s -= 1
    key[s] = 0

    for vertex in range(n):       
        minimum = float('inf')
        v = 0

        # Choose a vertex v that is not in visitedNode and has a minimum value in key
        for i in range(len(visitedNode)):
            if key[i] < minimum and visitedNode[i] == False:
                minimum = key[i]
                v = i    
        # Add vertex v to visited node
        visitedNode[v] = True

        # If the weight of the vertex u is greater than the previous sum value and has an edge and hasn’t been visited
        # Then update its value
        for u in range(n):
            if visitedNode[u] == False and graph[v][u] and (key[u] > key[v] + graph[v][u]):
                key[u] = key[v] + graph[v][u]

    # Store the results in array
    result = []
    for v in range(len(key)):
        # Do not include the source node weight
        if v != s:
            # If the weight of a vertex is 'inf' update it to -1
            if key[v] == float('inf'):
               result.append(-1)
            else:
                result.append(key[v])

    return result


print(shortestReach(4, [[3,1,3], [4,3,12], [4,1,20], [1,2,24]], 1))
print(shortestReach(4, [[1,2,5], [2,3,6], [3,4,2], [1,3,15]], 1))
print(shortestReach(5, [[1, 2, 10], [1, 3, 6], [2, 4, 8]], 2))