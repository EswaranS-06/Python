def B(X, Y, S, R):
    revY = Y[::-1]
    i = 0
    n = len(X)
    count_Y = 0
    count_revY = 0

    while i < n:
        max_len = 0
        used_reversed = False

        # Try to match the longest part of X[i:] in Y
        for j in range(i + 1, n + 1):
            if X[i:j] in Y:
                if j - i > max_len:
                    max_len = j - i
                    used_reversed = False
            if X[i:j] in revY:
                if j - i > max_len:
                    max_len = j - i
                    used_reversed = True

        if max_len == 0:
            return "Impossible"  # No match found

        if used_reversed:
            count_revY += 1
        else:
            count_Y += 1

        i += max_len  # Move forward by the matched length

    return count_Y * S + count_revY * R


x = input().lower()
y = input().lower()
sl, rl = [int(i) for i in input().split(" ")]

print(B(x,y,sl,rl))
