def print_table(n):
    # Print header row
    print("    |", end="")
    for i in range(1, n + 1):
        print(f"{i:>4}", end="")  # Right-align numbers
    print("\n" + "----+" + "----" * n)

    # Print table rows
    for row in range(1, n + 1):
        print(f"{row:>3} |", end="")
        for col in range(1, n + 1):
            print(f"{row * col:>4}", end="")
        print()  # Newline after each row

# Run the program
n = 5 #int(input("Enter the grid value: "))
print_table(n)
