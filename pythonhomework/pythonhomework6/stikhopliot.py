#размер - четырёхстопный ямб
import random

#открываем файл и записываем строки из него в список
def gettingfile():
    t=[]
    with open ('словник.txt','r',encoding='utf-8') as f:
        t=f.readlines()
    return t

#вызываем функцию getttingfile() и в полученном
#списке находим случайное слово с заданным тегом
def getcomponent(tag):
    a=[]
    for i in gettingfile():
        if tag in i:
            a.append(i[:i.find(tag)])
    return random.choice(a)

#составляем строку заданного типа
def getline(tags):
    s=[]
    for tag in tags:
        s.append(getcomponent(tag))
    capital=s[0][0]
    if not capital.isupper():
        capital=capital.upper()
    s[0]=capital+s[0][1:]
    line=''.join(s)
    return line[:len(line)-1]

#определяем, какой знак препинания поставить после строки
def getprep(line,iter):
    if 'Зачем' in line:
        return '?'
    elif 'Как так' in line:
        return '?!'
    elif iter==3:
        return '.'
    else:
        return ','
    

#определяем типы строк, состоящие из слов с заданными тегами
#многие теги похожи на Лейпцигские глоссы,
#но не все из них ими являются
def main():
    wordtags=[['N.M.anim','V.TR-M','N.-ACC','N-INSTR'],['CLIT1','N-GEN','ADV','N1','V.INTR'],\
              ['ADRB1','N.M.anim','V.INTR','ADJ-M'],['CLIT2','ADV','V-INF','ADRB2','N.-ACC']]
    for c in range(4):
        l=getline(random.choice(wordtags))
        print(l+getprep(l,c))
    input()
    return

if __name__=='__main__':
              main()

    
        
        
    

