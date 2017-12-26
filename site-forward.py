"""
Заменаяет существующие странцы сайта в директории на страницы для переадресации.
"""


import os
servername = 'learning-python.com'
homedir = 'books'
sitefilesdir = r'.\temp\public_html'
uploaddir = r'.\temp\isp-forward'
templatename = r'dataexamples\template.html'

try:
    os.mkdir(uploaddir)
except OSError: pass

temlate = open(templatename).read()
#получаем имена файлов без пути к ним
sitefiles = os.listdir(sitefilesdir)

count = 0
for filename in sitefiles:
    if filename.endswith('.html') or filename.endswith('.htm'):
        fwdname = os.path.join(uploaddir, filename)
        print('Creating', filename, 'as', fwdname)
        filetext = temlate.replace('$server$', servername)
        filetext = filetext.replace('$home$', homedir)
        filetext = filetext.replace('$file$', filename)
        open(fwdname, 'w').write(filetext)
        count += 1
print('Last file =>\n', filetext, sep='')
print('Done:', count, 'forward files created.')
