from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    threat = [a[i] for i in range(n)]
    edges = [[] for i in range(n)]
    parent = [i for i in range(n)]
    visited = [0 for i in range(n)]

    for i in range(n-1):
        v, u = map(int, input().split())
        # 0-index
        v -= 1
        u -= 1
        edges[v].append(u)
        edges[u].append(v)
    
    # BFS from root vertex
    # At each point, solution is a(i) or a(i) - a(parent) + threat(grandparent)
    queue = deque([0])
    while len(queue) > 0:
        v = queue.popleft()
        p = parent[v]
        visited[v] = 1
        
        if parent[v] != v and parent[p] != p:
            threat[v] = max(a[v], a[v] - a[p] + threat[parent[p]])
        for u in edges[v]:
            if visited[u] == 0:
                parent[u] = v
                queue.append(u)
    print(" ".join(map(str, threat)))