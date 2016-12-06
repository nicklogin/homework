with open ('freq.txt','r+',encoding='utf-8') as f:
    t=f.readlines()
    k=0.0
    for line in t:
        c=0
        for i in line:
            if i=='|':
                c+=1
        if c==2:
            word,part,freq=line.split('| ')
            if 'ед жен' in part:
                print(word,end=',')
                k+=float(freq)
    print(k)
    
        
