import re

#получаем массив предложений из текста:
def getsentences (filename):
    try:
        with open (filename, 'r', encoding = 'utf-8') as f:
            text = f.read()
        if text:
            #рег.выражение, метчащее предложения:
            smark = re.compile('\w.*?[.…!?\n]')
            sentences = re.findall(smark, text)
            if sentences:
                sentences = [punctcut(i) for i in sentences]
                sentences = [i for i in sentences if i]
            else:
                print('Предложений не найдено')
            return sentences
        else:
            print ('Выбран пустой текстовый файл')
            return False
    except UnicodeDecodeError:
        print('Неверная кодировка! Нужен файл в utf-8')

#удаляем пунктуацию из предложения, оставляем только пробелы:
def punctcut(s):
    words = re.findall('\w*-?\w*',s)
    if words:
        words = [i for i in words if i]
        return ' '.join(words)
    else:
        return ''

def main():
    upwordscheck = False
    sentences = getsentences(input('Введите имя файла:    '))
    if sentences:
        for sentence in sentences:
            if sentence.count(' ')>9:
                upwords=[i for i in sentence.split(' ') if i.istitle()]
                if upwords:
                    #каждая строка - слова из одного предложения
                    upwordscheck = True
                    print('{:^20}'.format(' '.join(upwords)))
        if not upwordscheck:
            print('Слов с большой буквы в предложениях длиннее 10 слов не найдено')

            
if __name__ == '__main__':
    main()
    
