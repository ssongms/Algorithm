jaeum = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
moeum = ['a', 'e', 'i', 'o', 'u']

while True:
    password = input()
    availPassword = False
    if password == "end":
        break

    for i in range(len(moeum)):
        if moeum[i] in password:
            availPassword = True # 아래에 있는 모든 if문을 통과하게 함
            break

    if availPassword:
        for j in range(len(password) - 2):
            if password[j] in moeum:
                if password[j+1] in moeum:
                    if password[j+2] in moeum:
                        availPassword = False
            if password[j] in jaeum:
                if password[j+1] in jaeum:
                    if password[j+2] in jaeum:
                        availPassword = False
        
    if availPassword:
        if any(word in password for word in ['aa','bb','cc','dd','eee','ff','gg','hh','ii','jj','kk','ll','mm','nn','ooo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz']):
            availPassword = False

    if availPassword:
        print("<" + password + "> is acceptable.")
    else:
        print("<" + password + "> is not acceptable.")