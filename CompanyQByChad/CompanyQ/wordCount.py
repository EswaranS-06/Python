def word_count(sentence):
    lst = sentence.split(" ")
    d = {}
    
    for i in lst:
        if not d.get(i):
            d.update({i:1})
        else:
            d.update({i:d.get(i)+1})
    print(d)


word_count("this is a test this is only a test") # → {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}