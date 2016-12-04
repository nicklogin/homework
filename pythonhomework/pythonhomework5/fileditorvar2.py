with open(input(),'r+', encoding='utf-8') as f:
#спрашиваем у пользователя путь к файлу
#например, source.txt(приложен к программе)
    allines=f.readlines()
    minlen=len(allines[0])
    maxlen=0
    
    for i in allines:
        if i and i!='\n':
            if len(i)>maxlen:
                maxlen=len(i)

            if len(i)<minlen:
                minlen=len(i)

    print(maxlen/minlen)
   
    
