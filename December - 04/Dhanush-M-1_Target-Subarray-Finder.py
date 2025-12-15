N, K = map(int, input().split())
arr = list(map(int, input().split()))

prefix_map = {0: -1}   # prefix_sum : index
current_sum = 0

for i in range(N):
    current_sum += arr[i]

    if (current_sum - K) in prefix_map:
        start = prefix_map[current_sum - K] + 1
        end = i
        print(start, end)
        break

    if current_sum not in prefix_map:
        prefix_map[current_sum] = i
else:
    print(-1, -1)
