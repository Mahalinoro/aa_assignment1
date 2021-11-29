# Prim's algorithm implementation to find MST of an undirected weighted graph
def prim(graph, n):
    # To keep track of vertices that are already been visited and included in MST
    visitedNode = [False] * n
    # To store the edges of the generated MST
    mst = []
    # To store the key value of the vertices
    # All the keys have been initialized to INFINITY only the 6th vertex to 0
    key = [float('inf')] * n
    key[5] = 0

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

        # If adjacent vertex u is less than the previous value in key and has an edge and hasn’t been visited
        for u in range(n):
            if visitedNode[u] == False and graph[v][u] and key[u] > graph[v][u]:
                key[u] = graph[v][u]
                mst.append([v,u])
    
    # Code to print the edges and weight
    print('Edges \t Weight')
    print('---------------')
    for pair in mst:
        if graph[pair[0]][pair[1]] in key:
            print(str(pair[0]+1) + ' -> ' + str(pair[1]+1) + '\t ' + str(graph[pair[0]][pair[1]]))


graph = [[0,28,0,0,0,10,0],
        [28,0,16,0,0,0,14],
        [0,16,0,12,0,0,0],
        [0,0,12,0,22,0,18],
        [0,0,0,22,0,25,24],
        [10,0,0,0,25,0,0],
        [0,14,0,18,24,0,0]]
n = 7
prim(graph, n) 

