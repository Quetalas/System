"""
Воссоздаёт файл, разреззаный с помощью split.py
Используйте python join.py --help для получения помощи.
"""

import os, sys
readsize = 1024


def join(fromdir, tofile):
    """
    Собирает файлы из указанной директории в единый указанный файл
    :param fromdir: директория в которой находятся части файла
    :param tofile: файл в который нужно собрать части
    :return: None
    """
    output = open(tofile, 'wb')
    parts = os.listdir(fromdir)
    parts.sort()
    sortedparts = []
    for filename in parts:
        sortedparts.append(int(filename[4:]))
    sortedparts.sort()
    for filenumber in sortedparts:
        filepath = os.path.join(fromdir, 'part' + str(filenumber))
        print('Track file: ', filepath)
        fileobj = open(filepath, 'rb')
        while True:
            filebytes = fileobj.read(readsize)
            if not filebytes: break
            output.write(filebytes)
        fileobj.close
    output.close()


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '--help':
        print('Use: join.py [from-dir-name to-file-name')
    else:
        if len(sys.argv) != 3:
            interactive = True
            fromdir = input('Directory containing part files? ')
            tofile = input('Name of file to be recreated? ')
        else:
            interactive = False
            fromdir, tofile = sys.argv[1:]
        absfrom, absto = map(os.path.abspath, [fromdir, tofile])
        print('Joining', absfrom, 'to make', absto)

        try:
            join(fromdir, tofile)
        except:
            print('Error joining files:')
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            print('Join complete: see', absto)
        if interactive: input('Press Enter key')