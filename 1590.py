import sys

input = sys.stdin.readline

N, T = map(int, input().split())
result = float('inf')

for _ in range(N):
    S, I, C = map(int, input().split())

    for k in range(C):
        arrival_time = S + I * k

        if arrival_time >= T:
            result = min(result, arrival_time - T)
        
print(result if result != float('inf') else -1)