import os
import re

def savedict(d, filename):
    with open(filename,'w', encoding='utf-8') as f:
        for key in d:
            line = key + '\t' + str(d[key])+'\n'
            f.write(line)
    return

def savearray(ar, filename):
    with open(filename,'w', encoding='utf-8') as f:
        for el in ar:
            line = '\t'.join(el)+'\n'
            f.write(line)
    return

def findbigrams(t):
    bigrams = []
    sentences = re.findall('<se>[\w\W]+?</se>', t)
    for sentence in sentences:
        bigram = ''
        raw_sentence = re.sub('<.*?>','',sentence)
        raw_sentence = re.sub('\n','',raw_sentence)
        words = re.findall('<w>[\w\W]+?</w>', sentence)
        for i in range(len(words)):
            if ('gr="PR' in words[i]) and (i<len(words)-1):
                if re.search('S,[\w\W]*?loc', words[i+1]):
                    bigram = re.sub('<.*?>','',words[i])+' '+re.sub('<.*?>','',words[i+1])
        if bigram:
            bigrams.append([bigram,raw_sentence])
    return bigrams
        
def task1():
    d = dict()
    path = '.\\news'
    for root, dirs, files in os.walk(path):
        for file in files:
            #print(file)
            with open (os.path.join(root,file), 'r', encoding = 'cp1251') as f:
                txt = f.read()
            d[file] = txt.count('<se>')
    savedict(d, 'sentencesnumber.csv')


def task2():
    lines = []
    lines.append(["Название файла", "Автор", "Тематика текста"])
    for root, dirs, files in os.walk(path):
        for file in files:
            nm = file
            with open (os.path.join(root,file), 'r', encoding = 'cp1251') as f:
                txt = f.read()
            author = re.search(r'<meta content="(.*?)" name="author">',txt).group(1)
            topic = re.search(r'<meta content="(.*?)" name="topic">',txt).group(1)
            lines.append([nm, author, topic])
    savearray(lines, 'authors_and_topics.csv')

def task3():
    corpus = ''
    for root, dirs, files in os.walk(path):
        for file in files:
            #print(file)
            with open (os.path.join(root,file), 'r', encoding = 'cp1251') as f:
                txt = f.read()
            corpus += txt
    bigrams = findbigrams(corpus)
    savearray(bigrams, 'bigrams.csv')
    
def main():
    task1()
    task2()
    task3()

if __name__ == '__main__':
    path = '.\\news'
    main()
