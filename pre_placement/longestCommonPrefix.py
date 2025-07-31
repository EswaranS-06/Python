def lcp(words):
    if not words:
        return ''
    word = min(words, key=len)
    stack = []
    end = 0
    for i in range(len(word)):
        for w in words:
            if w[i] != word[i]:
                end = 1
                break
        if end:
            break
        else:
            stack.append(word[i])
            
    return(''.join(stack))

t = [
  (['flow','flower','flight'], 'fl'),
  (['dog','racecar','car'], ''),
  ([], ''),
  (['single'], 'single'),
  (['','abc','ab'], ''),
  (['prefix','preach','prevent'], 'pre'),
  (['same','same','same'], 'same'),
  (['abc','abcd','ab'], 'ab'),
  (['a','a','a','a'], 'a'),
  (['longestcommonprefix','longest','long'], 'long'),
  (['interspace','internet','internal'], 'inter'),  # corrected
  (['flower','flow','flight','flute'], 'fl'),
  (['test','testing','tester','testify'], 'test'),
  (['zebra','apple','yellow'], ''),
  (['car','carb','carbon'], 'car'),
  (['abcd','abef','abxy'], 'ab'),
  (['one',''], ''),
  (['',''], ''),
  (['prefix','PREFIX'], ''),
  (['Case','casual'], ''),
  (['common','commune','communication'], 'comm'),
  (['a'*100,'a'*150,'a'*50], 'a'*50),
  (['ab','a','abc'], 'a'),
  (['xy','xz'], 'x'),
  (['sameprefix','same','sam'], 'sam'),
  (['flow','flown','flower','flow'], 'flow'),
  (['prefix','pre','pristine'], 'pr'),
  (['dog','dogma','do'], 'do'),
  (['alpha','alphabet','alphanumeric'], 'alpha'),
  (['tree','trie','trial'], 'tr'),
  ([''], ''),
  (['a','b'], ''),
  (['long','longer','longest','longevity'], 'long'),
  (['mix','maximum','mini'], 'm'),
  (['flower','flow','flask','flip'], 'fl'),
  (['prefixes','pre'], 'pre'),
  (['abcde','abxyz','ab123'], 'ab'),
  (['spoon','spoonful','spooky'], 'spoo'),
  (['hello','hell','heaven'], 'he'),
  (['abcd','efgh'], ''),
  (['same','same','diff'], ''),
  (['123','1234','12345'], '123'),
  (['!@#','!@','!@#$%'], '!@'),
  (['emoji😊','emoji😊test','emoji😊!'], 'emoji😊'),
  (['中文','中文测试','中文啊'], '中文'),
  (['repeat','repetitive','republic'], 'rep'),
  (['overlap','oven','oval'], 'ov'),
  (['sun','moon','star'], ''),
  (['prefix','preference','prevent','preview'], 'pre'),
  (['flower','flow','flop'], 'flo'),  # extra case
]
count = 0
for i in range(len(t)):
    o = lcp(t[i][0])
    r = t[i][1]
    print(f"Output: {o}, Result: {r}, IsMatch: {'Yes' if o == r else 'No'}")
    count = count + 1 if o == r else count + 0
    
print(count)