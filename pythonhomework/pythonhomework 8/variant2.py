import random

def getdictionary(a):
    with open(a,'r',encoding='utf-8') as f:
        x=f.readlines()
        d=dict()
        for line in x:
            line=[i for i in line.split(',')]
            d[line[0]]=line[1:]
    return d

def game(wordlist):
    keys=[i for i in wordlist.keys()]
    word=random.choice(keys)
    t=True
    #создаем строку, где точек столько, сколько букв в слове:
    points=''.join(['.']*len(word))
    while t:
        print(random.choice(wordlist[word])+' '+points+' ?')
        ans=input().lower()
        if ans==word:
            print('Правильно !')
            t=False
        else:
            print('Неправильно. Ещё одну попытку ?')
            r=input().lower()
            while r!='да':
                if r=='нет':
                    return
                else:
                  print('Неверный ввод, введите "да" или "нет" ')
                  r=input().lower()
    return

def main():
    print('Сыграем в игру ?')
    a=input().lower()
    while a!='нет':
        if a.lower()=='да':
            #запускаем игру:
            game(getdictionary('Слова и подсказки.csv'))
            print('Cыграем ещё раз ?')
            a=input().lower()
            continue
        elif a!='нет':
            print('Неверный ввод, введите "да" или "нет" ')
            a=input().lower()
    print('До свидания !')

if __name__=='__main__':
             main()
    
