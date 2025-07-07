def most_frequent(lst):
    d = {}
    lst.sort()
    for i in lst:
        if not d.get(i):
            d.update({i:1})
        else:
            d.update({i:d.get(i)+1})
    print(max(d, key=d.get))

most_frequent([1, 3, 2, 1, 4, 1, 3])