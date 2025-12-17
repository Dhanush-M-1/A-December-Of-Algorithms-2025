n = int(input("Enter n: "))

if n % 2 == 0:
    print("Magic square is only possible for odd values of n.")
else:
    magic_constant = n * (n * n + 1) // 2
    print("Magic constant:", magic_constant)

    magic_square = [[0] * n for _ in range(n)]

    i = 0
    j = n // 2

    for num in range(1, n * n + 1):
        magic_square[i][j] = num

        next_i = (i - 1) % n
        next_j = (j + 1) % n

        if magic_square[next_i][next_j] != 0:
            i = (i + 1) % n
        else:
            i = next_i
            j = next_j

    for row in magic_square:
        for val in row:
            print(f"{val:4}", end="")
        print()
