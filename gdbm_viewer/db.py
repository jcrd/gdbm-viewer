import dbm.gnu
import sys

import pyinotify


def bstr(b):
    return str(b, sys.stdout.encoding)


class DB(pyinotify.ProcessEvent):
    def __init__(self, path, callback):
        self.path = path
        self.callback = callback

        wm = pyinotify.WatchManager()
        wm.add_watch(self.path, pyinotify.IN_CLOSE_WRITE)

        self.notifier = pyinotify.ThreadedNotifier(wm, self)
        self.notifier.daemon = True
        self.notifier.start()

        callback(self.read())

    def __del__(self):
        self.notifier.stop()

    def read(self):
        d = {}
        with dbm.open(self.path, "r") as db:
            k = db.firstkey()
            while k is not None:
                d[bstr(k)] = bstr(db[k])
                k = db.nextkey(k)

        return d

    def process_IN_CLOSE_WRITE(self, _):
        self.callback(self.read())
