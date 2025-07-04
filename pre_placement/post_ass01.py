def maxAbsoluteDifference(arr):
    n = len(arr)
    
    # Arrays to store nearest smaller left and right
    ls = [0] * n
    rs = [0] * n

    # Find nearest smaller to LEFT
    stack = []
    for i in range(n):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            ls[i] = stack[-1]
        else:
            ls[i] = 0
        stack.append(arr[i])

    # Find nearest smaller to RIGHT
    stack = []
    for i in range(n-1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            rs[i] = stack[-1]
        else:
            rs[i] = 0
        stack.append(arr[i])

    # Compute max absolute difference
    max_diff = 0
    for i in range(n):
        diff = abs(ls[i] - rs[i])
        max_diff = max(max_diff, diff)

    return max_diff


# Example usage:

print(maxAbsoluteDifference([2,4,8,7,7,9,3]))