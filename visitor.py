import os
import sys

class FileVisitor:
    """
    Выполняет олбход всех файлов, не являющихся каталогами,
    ниже startDir(по умолчанию '.')
    """
    def __init__(self, context=None, trace=2):
        self.fcount = 0
        self.dcount = 0
        self.context = context
        self.trace = trace

    def run(self, startDir=os.curdir, reset=True):
        if reset: self.reset()
        for (thisDir, dirsHere, filesHere) in os.walk(startDir):
            self.visitdir(thisDir)
            for fname in filesHere:
                fpath = os.path.join(thisDir, fname)
                self.visitfile(fpath)

    def reset(self):
        self.fcount = self.dcount = 0

    def visitdir(self, dirpath):
        """
        Вызывается для каждого каталога.
        Переопределите или расширьте
        :param dirpath:
        :return:
        """
        self.dcount += 1
        if self.trace > 0: print(dirpath, '...')

    def visitfile(self, filepath):
        """
        Вызывается для каждого файла.
        Переопределите или расширьте
        :param filepath:
        :return:
        """
        self.dcount += 1
        if self.trace > 0: print(filepath, '...')


class SearchVisitor(FileVisitor):
    """
    Выполняет поиск строки в файлах, находящихся в таклоге
    startDir и ниже;
    """
    skopexts = []
    #допустимые расширения
    textexts = ['.txt', '.py', '.pyw', '.html', '.c', '.h']
    skipexts = ['.gif', '.jpg', '.pyc', '.o', '.a', '.exe']

    def __init__(self, searchkey, trace=2):
        FileVisitor.__init__(self, searchkey, trace)
        self.scount = 0
        self.skiped = []

    def reset(self):
        self.scount = 0

    def candidate(self, fname):
        ext = os.path.splitext(fname)[1]
        if self.textexts:
            return ext in self.textexts
        else:
            return ext not in self.skipexts

    def visitfile(self, fname):
        FileVisitor.visitfile(self, fname)
        if not self.candidate(fname):
            if self.trace > 0: print('Skipping', fname)
        else:
            try:
                text = open(fname).read()
                if self.context in text:
                    self.visitmatch(fname, text)
                    self.scount += 1
            except:
                self.skiped.append(fname)
                print("Error", sys.exc_info()[0], sys.exc_info()[1])


    def visitmatch(self, fname, text):
        print('{0} has {1}'.format(fname, self.context))


if __name__ == '__main__':
    dolist = 1
    dosearch = 2
    donext = 4


    def selftest(testmask):
        if testmask & dolist:
            visitor = FileVisitor(trace=2)
            visitor.run(sys.argv[2])
            print('Visited {0} files and {1} dirs'.format(visitor.fcount, visitor.dcount))
        if testmask & dosearch:
            visitor = SearchVisitor(sys.argv[3], trace=0)
            visitor.run(sys.argv[2])
            print('Found in {0} files, visited {1}'.format(visitor.scount, visitor.fcount))
            print('Skiped {0} files:'.format(len(visitor.skiped)))
            for sk in visitor.skiped:
                print('***** Skip:', sk)


    selftest(int(sys.argv[1])) # 3 = dolist | dosearch
