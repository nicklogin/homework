import os
import re

def savedict(d, filename):
    with open(filename,'w', encoding='utf-8') as f:
        for key in d:
            line = key + '\t' + str(d[key])+'\n'
            f.write(line)
    #print('dictionary successfully saved')
    return

def savearray(ar, filename):
    with open(filename,'w', encoding='utf-8') as f:
        for el in ar:
            line = '\t'.join(el)+'\n'
            f.write(line)
    #print('dictionary successfully saved')
    return

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

def main():
    task1()
    task2()

def task2():
    lines = []
    lines.append(["Название файла", "Автор", "Тематика текста"])
    for root, dirs, files in os.walk(path):
        for file in files:
            nm = file
            print(nm)
            with open (os.path.join(root,file), 'r', encoding = 'cp1251') as f:
                txt = f.read()
            author = re.search(r'<meta content="(.*?)" name="author">',txt).group(1)
            topic = re.search(r'<meta content="(.*?)" name="topic">',txt).group(1)
            lines.append([nm, author, topic])
    savearray(lines, 'authors_and_topics.csv')
    

if __name__ == '__main__':
    path = '.\\news'
    main()
