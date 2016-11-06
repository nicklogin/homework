word=''
#запрашиваем у пользователя ввод, пока не будет введено слово без пробелов
while word=='':
    print('Введите 1 русское слово(без пробелов):')
    word=input()
    if word:
        for i in word:
            if i==' ':
                print('Нужно ввести слово без пробелов')
                word=''
                break
        if word=='':
            continue
        for index,elem in enumerate(word):
            if index%2==0 and (elem=='о' or elem=='п' or elem=='е'):
                print(elem,end=' ')
    else:
        print('Нужно ввести слово') 
