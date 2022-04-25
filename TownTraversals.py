graph = {
    'A': ['School','Hospital','MNC 1','Mall','Police Station','H7','H6','H5','Factory','Flat 1','Flat 2','B'],
    'Hospital': ['H1','H3'],
    'Mall': ['Museum','MNC 1','MNC 2'],
    'MNC 1': ['Museum'],
    'MNC 2': ['Museum'],
    'Museum': ['Library'],
    'Library': ['H1','H3'],
    'H1': ['H2'],
    'H3': ['H4'],
    'H2': ['Pool'],
    'H4': ['Pool'],
    'Pool': [],
    'Factory': ['Library'],
    'H5': [],
    'H6': [],
    'H7': [],
    'School': ['Field','Police Station','Post Office'],
    'Police Station': ['Post Office'],
    'Field': [],
    'Post Office': [],
    'Flat 1': [],
    'Flat 2': [],
    'B': ['Flat 1','Flat 2','H7','H6','H5','Factory','Police Station','Mall','MNC 1','Hospital','School']
}

listBFS, listDFS = [], []
visitedDFS = set()
visitedBFS = []
queue = []


def bfs(visitedBFS, graph, node):
    visitedBFS.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        listBFS.append(s)

        for neighbour in graph[s]:
            if neighbour not in visitedBFS:
                visitedBFS.append(neighbour)
                queue.append(neighbour)

    return listBFS


def dfs(visitedDFS, graph, node):
    if node not in visitedDFS:
        listDFS.append(node)
        visitedDFS.add(node)
        for neighbour in graph[node]:
            dfs(visitedDFS, graph, neighbour)
    return listDFS


# Driver Code
start = input()
B = bfs(visitedBFS, graph, start)
D = dfs(visitedDFS, graph, start)

BFSsequence, DFSsequence = '', ''

for i in B:
    BFSsequence += i + ' \u2192 '
for i in D:
    DFSsequence += i + ' \u2192 '

print("BFS sequence: ", BFSsequence[:-3])
print("DFS sequence: ", DFSsequence[:-3])