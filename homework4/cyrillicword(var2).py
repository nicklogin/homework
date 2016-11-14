word=''
#запрашиваем у пользователя ввод, пока не будет введено cлово кириллицей
#без пробелов и других знаков
while word=='':
    print('Введите 1 русское слово(без пробелов и знаков препинания):')
    word=input()
    if word:
        for i in word:
            if ord(i)<128 or 175<ord(i)<224 or ord(i)>241:
                print('Слово может содержать только кириллические буквы без пробелов и др. знаков')
                word=''
                break
        if word=='':
            continue
        for index,elem in enumerate(word):
            if index%2==0 and (elem=='о' or elem=='п' or elem=='е'):
                print(elem,end=' ')
    else:
        print('Нужно ввести слово') 
