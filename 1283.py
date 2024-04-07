import sys

# 1. 스페이스바를 기준으로 스플릿하여 리스트1에 저장
# 2. 리스트1을 순회하며 리스트1[0] 을 검사하여 단축키로 지정된 것이 있는지 확인
# 2-1. 단축키로 지정된 것이 없으면 해당 요소를 바로 단축키로 저장, 인덱스를 따로 저장함
# 2-2. 단축키로 전부 지정돼있다면 리스트1을 순회하며 지정한 단축키가 없을때까지 이동 (단 단어의 첫글자는 제외)
# 2-2-1. 이동이 완료되었으면 해당 요소를 단축키로 저장

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