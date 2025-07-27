def parse_grid():
    grid = []
    cell_type = []
    for _ in range(9):
        row = input().split()
        g_row = []
        t_row = []
        for val in row:
            if val.startswith("0"):  # Tina-filled
                g_row.append(int(val[1]))
                t_row.append("tina")
            elif val.endswith("0"):  # Hint cell
                g_row.append(int(val[:-1]))
                t_row.append("hint")
            else:  # Pre-filled
                g_row.append(int(val))
                t_row.append("fixed")
        grid.append(g_row)
        cell_type.append(t_row)
    return grid, cell_type

def get_box_index(i, j):
    return (i // 3) * 3 + (j // 3)

def solve():
    grid, cell_type = parse_grid()
    hint_nums = set(map(int, input().split()))
    k = int(input())

    wrong_cells = []

    for i in range(9):
        for j in range(9):
            val = grid[i][j]
            is_wrong = False

            # Skip if this cell is empty (not possible here as 0s aren't in the input grid values)
            if val == 0:
                is_wrong = True

            # Validate rows
            for col in range(9):
                if col != j and grid[i][col] == val:
                    is_wrong = True

            # Validate cols
            for row in range(9):
                if row != i and grid[row][j] == val:
                    is_wrong = True

            # Validate 3x3 box
            bi = (i // 3) * 3
            bj = (j // 3) * 3
            for r in range(bi, bi + 3):
                for c in range(bj, bj + 3):
                    if (r != i or c != j) and grid[r][c] == val:
                        is_wrong = True

            # For hint cells, check if value is in hint_nums
            if cell_type[i][j] == "hint" and val not in hint_nums:
                is_wrong = True

            # Only count as wrong if it's not a fixed cell
            if is_wrong and cell_type[i][j] != "fixed":
                wrong_cells.append((i, j))

    if not wrong_cells:
        print("Won")
    elif len(wrong_cells) > k:
        print("Impossible")
    else:
        for i, j in sorted(wrong_cells):
            print(f"{i} {j}")

solve()
