import sys
N = int(sys.stdin.readline())
shortcutKeys = []
result = []

for _ in range(N):
    isFirst = False
    words = input() # words => "Save As"
    splitWords = list(words.split(" ")) #splitWords -> ['Save', 'As']

    for idx, word in enumerate(splitWords): # word -> 'Save'
        if word[0].upper() not in shortcutKeys:
            shortcutKeys.append(word[0].upper())
            splitWords[idx] = "[" + str(word[0]) + "]" + word[1:]
            isFirst = True
            break
    
    modifyIdx = -1
    if not isFirst: # 단어의 첫 문자가 단축키가 될 수 없을 때
        for idx, wordChar in enumerate(words):
            if wordChar.upper() not in shortcutKeys and wordChar != " ":
                shortcutKeys.append(wordChar.upper())
                modifyIdx = idx
                break
                
    if modifyIdx != -1 and not isFirst: # 인데스를 기반으로 [, ]를 앞 뒤로 추가하는 로직
        shorcutKey = words[modifyIdx]
        words = words[0:modifyIdx] + "[" + shorcutKey + "]" + words[modifyIdx+1:]

    if isFirst:
        result.append(" ".join(splitWords))
    else:
        result.append(words)

for solve in result:
    print(solve)