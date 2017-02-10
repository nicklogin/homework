import re

def getxt():
    with open(input('Введите имя входного файла: '),'r',encoding='utf-8') as f:
        text=f.read()
    return text

def printinf(s):
    with open(input('Введите имя выходного файла: '),'w',encoding='utf-8') as f:
        f.write(s)
    return

def main():
    a=r'<table class="infobox vcard"[\s\S]*?<tr>[\s\S]*?<.*?>Часовой пояс([\s\S]*?)</tr>'
    b=r'(<.*?>)([^<>]*)'
    timezone=re.search(a,getxt()).group(1)
    onlywords=re.findall(b,timezone)
    timezone=''
    for i in onlywords:
        timezone+=i[1]
    printinf(timezone)

if __name__=='__main__':
    main()
  
    
