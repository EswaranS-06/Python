def res():
    s = ['h','e','l','l','o']
    l = 0
    r = len(s)-1
    print(s.sort(reverse=T))

    while l!=r:
        
        s[l],s[r] =s[r],s[l]
        l = l + 1
        r = r - 1
        
    print(s)
res()
