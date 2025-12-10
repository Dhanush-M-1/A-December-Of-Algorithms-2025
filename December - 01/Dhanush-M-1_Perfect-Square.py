N = int(input())
squares = []
i = 1
while i*i <= N:
    squares.append(i*i)
    i += 1
print(*squares)
print(len(squares))