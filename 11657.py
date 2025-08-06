import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edges = []
index = 2
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

INF = int(1e9)
dist = [INF] * (N + 1)
dist[1] = 0

for _ in range(N - 1):
    for a, b, c in edges:
        if dist[a] != INF and dist[b] > dist[a] + c:
            dist[b] = dist[a] + c

has_cycle = False
for a, b, c in edges:
    if dist[a] != INF and dist[b] > dist[a] + c:
        has_cycle = True
        break

if has_cycle:
    print(-1)
else:
    for i in range(2, N + 1):
        print(dist[i] if dist[i] != INF else -1)
 