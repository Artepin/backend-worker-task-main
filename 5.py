import fnmatch
import os
from pathlib import Path

def task1():
    # в папке test найти все файлы filenames вывести колличество
    name_to_find ='filenames'
    for root, dirs, files in os.walk("test"):
        for filename in files:
            if name_to_find in filename:
                print(filename)
    print()
    pass


def task2():
    # в папке test найти все email адреса записанные в файлы
    emails = []
    email = "@"
    my_files = []
    for root, dirs, files in os.walk("test"):
        for filename in files:
            p = os.path.abspath(os.path.join(root,filename))
            test = os.path.getsize(p)
            if os.stat(p).st_size!=0:
                my_files.append(p)
                with open(root+ '/'+ filename, 'r') as file:

                    local_file = file.readlines()
                    for i in local_file:
                        if email in i:
                            emails.append(i)

    for i in emails:
        print(i)
    pass


def main():
    task1()
    task2()
    # дополнительно: придумать механизм оптимизации 2-й задачи

    #механизм оптимизации заключается в том, что без открытия файла мы смотрим сначала его размер, а потом уже, если файл не пуст, его проверяем.


if __name__ == '__main__':
    main()
