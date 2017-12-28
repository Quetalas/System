"""
Проигрывает медиафайлы.
"""
import os, sys, mimetypes, webbrowser

helpmsg = """
Sorry: can't find a media player for {0} on your system!
Add an entry for your system to the ,edia player dictionary
for this type of file in playfile.py, of play the file manually.
"""


def trace(*args): print(*args)


class MediaTool:
    def __init__(self,runtext=''):
        self.runtext = runtext

    def run(self, mediafile, **options):
        fullpath = os.path.abspath(mediafile)
        self.open(fullpath, **options)

class Filter(MediaTool):
    def open(self, mediafile, **ignored):
        media = open(mediafile, 'rb')
        #запустить команду оболочки
        player = os.popen(self.runtext, 'w')
        player.write(media.read())

class Cmdline(MediaTool):
    def open(self, mediafile, **ignored):
        cmdline = self.runtext.format(mediafile)
        os.system(cmdline)

class Winstart(MediaTool):
    def open(self, mediafile, wait=False, **other):
        if not wait:
            os.startfile(mediafile)
        else:
            os.system('start /WAIT ' + mediafile)

class Webbrowser(MediaTool):
    def open(self, mediafile, **options):
        webbrowser.open_new('file://{0}'.format(mediafile), **options)

audiotools = {
    'win32': Winstart()
}

videotools = {
    'win32': Winstart()
}

imagetools = {
    'win32': Winstart()
}

texttools = {
    'win32': Cmdline('notepad {0}')
}

apptools = {
    'win32': Winstart()
}

mimetable ={'audio': audiotools,
            'video': videotools,
            'image': imagetools,
            'text': texttools,
            'application': apptools}


def trywebbrowser(filename, helpmsg=helpmsg, **options):
    trace('trying browser', filename)
    try:
        player = Webbrowser()
        player.run(filename, **options)
    except:
        print(helpmsg.format(filename))


def playknownfile(filename, playertable={}, **options):
    if sys.platform in playertable:
        playertable[sys.platform].run(filename, **options)
    else:
        trywebbrowser(filename, **options)


def playfile(filename, mimetable=mimetable, **options):
    contenttype, encoding = mimetypes.guess_type(filename)
    if contenttype == None or encoding is not None:
        contenttype = '?/?'
    maintype,sybtype = contenttype.split('/', 1)
    if maintype in mimetable:
        playknownfile(filename, mimetable[maintype], **options)
    else:
        trywebbrowser(filename, **options)


if __name__ == '__main__':
    trywebbrowser(r'C:\Users\Public\Videos\Sample Videos\Wildlife.wmv')