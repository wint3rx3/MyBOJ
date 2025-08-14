import sys
input = sys.stdin.readline

N, K = map(int, input().split())
wheel = ['?'] * N
pos = 0                      
used = {}

ok = True
for _ in range(K):
    S, ch = input().split()
    S = int(S)

    pos = (pos - S) % N
    if wheel[pos] != '?' and wheel[pos] != ch:
        ok = False
        break

    if ch in used and used[ch] != pos:
        ok = False
        break

    wheel[pos] = ch
    used[ch] = pos

if not ok:
    print("!")
else:
    ans = []
    for i in range(N):
        ans.append(wheel[(pos + i) % N])
    print(''.join(ans))
