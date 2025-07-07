def str_compress(st):
    lst = [i for i in st]

    c = lst[0]
    stack = [c]
    sc = ""
    for i in range(1,len(lst)):
        if lst[i] == c:
            stack.append(lst[i])
        else:
            sc += c + str(len(stack))
            stack.clear()
            c = lst[i]
            stack.append(c)
            
    sc += c + str(len(stack))
    print(sc)
    
str_compress('aaabbcaabb')

# def str_compress(st): <--- By Chad
#     if not st:
#         return ""

#     compressed = ""
#     count = 1
#     for i in range(1, len(st)):
#         if st[i] == st[i - 1]:
#             count += 1
#         else:
#             compressed += st[i - 1] + str(count)
#             count = 1

#     compressed += st[-1] + str(count)

#     return compressed if len(compressed) < len(st) else st
