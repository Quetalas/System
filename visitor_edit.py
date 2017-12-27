import os, sys
from visitor import SearchVisitor

class EditVisitor(SearchVisitor):
    """
    Открывает для редактирования файлы, содержащие искомую
    строку и находящиеся в катологе startDir или ниже
    """
    editor = r'C:\Windows\system32\notepad.exe'

    def visitmatch(self, fpathname, text):
        os.system('{0} {1}'.format(self.editor, fpathname))


if __name__ == '__main__':
    visitor = EditVisitor(sys.argv[1])
    visitor.run('.' if len(sys.argv) < 3 else sys.argv[3])
    print('Edited {0} files, visited {1}, skipped {2}'.format(visitor.scount, visitor.fcount, len(visitor.skiped)))