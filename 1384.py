import sys

lines = sys.stdin.read().splitlines()
idx = 0
group_no = 1
outputs = []

while idx < len(lines):
    line = lines[idx].strip()
    idx += 1

    if not line:
        continue
    if line == '0':
        break

    n = int(line)
    names = []
    rows = []

    for _ in range(n):
        parts = lines[idx].strip().split()
        idx += 1
        names.append(parts[0])
        rows.append(parts[1:])

    group_lines = [f"Group {group_no}"]
    nasty_found = False

    for i in range(n):
        for t, mark in enumerate(rows[i]):
            if mark == 'N':
                a = (i - 1 - t) % n
                group_lines.append(f"{names[a]} was nasty about {names[i]}")
                nasty_found = True

    if not nasty_found:
        group_lines.append("Nobody was nasty")

    outputs.append("\n".join(group_lines))
    group_no += 1

print("\n\n".join(outputs))
