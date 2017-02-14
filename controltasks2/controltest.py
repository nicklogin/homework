import re
#задание1
def task1(filename):
    with open (filename, 'r', encoding='utf-8') as f:
        l=len(f.readlines())
    with open ('Stringnumber.txt', 'w', encoding='utf-8') as t:
        t.write('The number of strings is '+str(l))
    return
#pflfybt2
def task2(filename):
    d=dict()
    with open(filename,'r',encoding='utf-8') as f:
        text=f.read()
    t=re.compile(r'<w.*?type="(.*?)"')
    types=re.findall(t,text)
    for i in types:
        d[i]=types.count(i)
    with open('types.txt','w',encoding='utf-8') as x:
        for typ in d.keys():
            x.write(typ+'\n')
    return

def htmtoxml(text):
    w=re.compile(r'<w lemma="(.*?)".*?type="(.*?)">(.*?)</w>')
    words=re.findall(w,text)
    with open ('f.csv','w',encoding='utf-8') as f:
        for i in words:
            f.write(','.join(i)+'\n')
    return
#задание3        
def task3(filename):
    d=dict()
    with open(filename,'r',encoding='utf-8') as f:
        text=f.read()
    t=re.compile(r'<w.*?type="(..f.*?)"')
    types=re.findall(t,text)
    for i in types:
        d[i]=types.count(i)
    with open('typesnumber.txt','w',encoding='utf-8') as x:
        for key in d.keys():
            x.write(key+' - '+str(d[key])+'\n')
    htmtoxml(text)
    return
    
def main():
    task1('f.xml')
    task2('f.xml')
    task3('f.xml')
    

if __name__=='__main__':
    main()
