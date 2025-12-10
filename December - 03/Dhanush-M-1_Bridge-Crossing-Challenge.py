# December 03 - Bridge Crossing Challenge

line = input().strip()          
line = line.replace("stones", "").replace("=", "").strip()
stones = eval(line)              

n = len(stones)
max_reach = 0

for i in range(n):
    if i > max_reach:
        print("false")
        break

    max_reach = max(max_reach, i + stones[i])

    if max_reach >= n - 1:
        print("true")
        break
else:
    print("true" if max_reach >= n - 1 else "false")
