import sys
input = sys.stdin.readline

N = int(input())
numbers = []

for _ in range(N):
    line = input().strip()
    current = ''
    
    for c in line:
        if c.isdigit():
            current += c
        else:
            if current:
                numbers.append(int(current))
                current = ''
    if current:
        numbers.append(int(current))

numbers.sort()

for num in numbers:
    print(num)
