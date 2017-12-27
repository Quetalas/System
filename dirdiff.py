"""
Уникальные для двух калогов имена файлов и папок в них
"""
import os, sys

def reportdiffs(unique1, unique2, dir1, dir2):
    """
    Генерирует отчёт о различиях файлов в двух директориях
    :param unique1: уникальные файлы первой директории
    :param unique2: уникальные файлы второй директории
    :param dir1: первая директория
    :param dir2: вторая директория
    :return:
    """
    if not (unique1 or unique2):
        print('Directory lists are identical')
    else:
        if unique1:
            print('Files unique to', dir1)
            for file in unique1:
                print('...', file)
        if unique2:
            print('Files unique to', dir2)
            for file in unique2:
                print('...', file)


def diffetence(seq1, seq2):
    """
    Возвращает элементы присутвствующие только в seq1;
    Не теряет порядок следования элементов
    :param seq1:
    :param seq2:
    :return:
    """
    return [item for item in seq1 if item not in seq2]


def comparedis(dir1, dir2, files1=None, files2=None):
    """
    Сравнивает содержимое каталогов, но не сравнивает содержимое файлов;
    :param dir1:
    :param dir2:
    :param files1:
    :param files2:
    :return: True если нет различий
    """
    print('Comparing', dir1, 'to', dir2)
    files1 = os.listdir(dir1) if files1 is None else files1
    files2 = os.listdir(dir2) if files2 is None else files2
    unique1 = diffetence(files1, files2)
    unique2 = diffetence(files2, files1)
    reportdiffs(unique1, unique2, dir1, dir2)
    return not ( unique1 or unique2)


def getargs():
    try:
        dir1, dir2 = sys.argv[1:]
    except:
        print('Usage: dirdiff.py dir1 dir2')
        sys.exit(1)
    else:
        return (dir1, dir2)


if __name__ == '__main__':
    dir1, dir2 = getargs()
    comparedis(dir1, dir2)