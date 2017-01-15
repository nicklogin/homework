def getwords(filename):
    with open (filename,'r',encoding='utf-8') as f:
        text=f.read()
        words=[i.strip(',!.";:()-«»') for i in text.split(' ')]
    return words

def wordswithending(words,a):
               m=[]
               c=0
               for word in words:
                   if len(word)>len(a):
                       if word[len(word)-len(a):]==a:
                           if not word in m:
                               c+=1
                           m.append(word)
               print ('Количество разных слов с окончанием -'+a+' в тексте: ',c)
               return m

def maxwordfrequency(m):
               freqs=[]
               for i in range(len(m)):
                   freqs.append(0)
                   for word in m:
                       if m[i]==word:
                           freqs[i]+=1
               maxind=0
               for i in range(len(freqs)):
                   if freqs[i]>maxind:
                       maxind=i
               return m[maxind]

def main():
    x=maxwordfrequency(wordswithending(getwords(input('Введите имя файла: ')),'ness'))
    print('Слово с максимальной частотой: ',x)

if __name__=='__main__':
               main()
               
