import re

def getwords(filename):
    with open (filename,'r',encoding='utf-8') as t:
        text=t.readlines()
        words=set()
        for line in text:
            if line and line!='\n':
                lw=[i.strip(',.!()[]{};:""?<>-\n') for i in line.split(' ')]
                for w in lw:
                    if w:
                        words.add(w.lower())
    return words

def main():
    f=re.compile('на(ш(л[аои]|е(л|дший?)|ёл)|й(ти|д(и(те)?|ут?|[её](нн(ый|ое|ая)|шь|те?|м)|я)))')
    words=getwords(input('Введите имя файла:  '))
    forms=set()
    for word in words:
        if f.match(word)!=None:
            forms.add(word)
    for i in forms:
        print(i)

if __name__=='__main__':
    main()


