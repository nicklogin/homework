import re
import os
import shutil

def printfilenames(path):
    #здесь храним неповторяющиеся имена файлов:
    printed = []
    counter = 0
    for i in os.listdir(path):
        if os.path.isfile(i):
            a = i[:i.rfind('.')]
            if a not in printed:
                print(i)
                printed.append(a)
            if not re.search('[0-9]',a):
                counter += 1
        else:
            if i not in printed:
                print(i)
                printed.append(i)
    print('Количество файлов, не содержащих цифры в названии = ', counter)
    return

def main():
    printfilenames('.')
                
if __name__ == '__main__':
    main()

