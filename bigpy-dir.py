"""
Находит самый большой файл с исходныи кодом Python в каталоге.
Если в аргементе командой строки не был указан каталог, то ищет в
стандартной библиотеке Python для Windows
"""

import os
import glob
import sys

dirname = r'C:\Python35\Lib'
allpy = glob.glob(dirname + os.sep + '*.py')
max = 0
maxname = ''
for filename in allpy:
    filesize = os.path.getsize(filename)
    if filesize > max:
        max = filesize
        maxname = filename

print(max)
print(maxname)
