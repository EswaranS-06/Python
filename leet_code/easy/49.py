def ssdf(strs):
    d = {}
    res = []
    for s in strs:
        lst_str = [i for i in s]
        lst_str.sort()
        so_str = "".join(lst_str)
        if so_str in d:
            d[so_str].append(s)
        else:
            d.update({so_str:[s]})
            
    for i in d.values():
        res.append(i)
        
    return(res)

s = 'hello'
s1 = 'eollh'
lst = [s,s1]
print(ssdf(["eat","tea","tan","ate","nat","bat"]))