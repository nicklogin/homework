slova=[]
s=input('Введите слово:')
while s:
    slova.append(s)
    s=input('Введите слово:')
with open ('freq.txt','r+',encoding='utf-8') as f:
    t=f.readlines()
    for slovo in slova:
        x=0
        for line in t:
            c=0
            for i in line:
                if i=='|':
                    c+=1
            if c==2:
                word,part,freq=line.split('| ')
                if word==slovo+' 'or word==slovo:
                    print(part,freq,sep=';',end='\n')
                    x=1
        if x==0:
            print('Слово '+slovo+' в словаре отсутствует.')
            

