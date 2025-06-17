if __name__ == '__main__':
    names = []
    scores = []
    for i in range(int(input())):
        names.append(input())
        scores.append(float(input()))
        
    name = []
    s = sorted(list(set(scores)))
    for i in range(len(scores)):
        if scores[i] == s[1]:
            name.append(names[i])
    
    name.sort()
    for i in name:
        print(i)