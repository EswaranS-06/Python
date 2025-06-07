def print_star_triangle(n):
    for i in range(1, n + 1):
        spaces = '   ' * (n - i)         # 3 spaces per gap for alignment
        stars = '  *' * i                # each star with 2 spaces before
        print(spaces + stars)

# Input from user
rows = int(input("Enter number of rows: "))
print_star_triangle(rows)
