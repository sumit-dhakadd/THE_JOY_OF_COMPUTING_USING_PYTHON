def View(lst, n):
    for i in range(n):
        for j in range(n):
            print(lst[i][j], end=" ")
        print()
    print()  # add a blank line for better readability

def Magic_Square(n):
    Matrix = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        Matrix.append(l)
    
    i = n // 2
    j = n - 1
    num = n * n
    count = 1

    while count <= num:
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1

        if Matrix[i][j] != 0:
            j = j - 2
            i = i + 1
            continue
        else:
            Matrix[i][j] = count
            count += 1

        i = i - 1
        j = j + 1

    # display magic square
    print(f"Magic Square of size {n}x{n}:\n")
    View(Matrix, n)

    # magic constant
    print("The sum of each Row/Column/Diagonal :", int(n * ((n**2 + 1) / 2)))
    print("-" * 50)

# ---- MAIN ----
Magic_Square(3)
Magic_Square(7)
