import re

def getxt():
    with open('Викинги — Википедия.htm','r',encoding='utf-8') as f:
        text=f.read()
    return text

def writxt(s):
    with open('Бурундукинги — Википедия.htm','w',encoding='utf-8') as f:
        f.write(s)
    return

def main():
    text=getxt()
    text=re.sub(r'викинг',r'бурундук',text)
    text=re.sub(r'Ви(.?)кинг(.*?)(\b)',r'Бурундук\2\1\3',text)
    #print(text)
    writxt(text)

if __name__=='__main__':
    main()
  
    
