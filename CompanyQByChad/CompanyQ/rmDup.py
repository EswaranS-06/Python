def remove_duplicates(lst):
    res = []
    for i in lst:
        if i in res:
            continue
        else:
            res.append(i)
            
    return res

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))