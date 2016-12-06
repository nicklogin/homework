with open ('freq.txt','r+',encoding='utf-8') as f:
    t=f.readlines()
    for line in t:
        c=0
        for symbol in line:
          if symbol=='|':
                c+=1
        if c==2:
            word,part,freq=line.split('| ')
            if 'союз' in part:
                print(line,end='\n')
            

