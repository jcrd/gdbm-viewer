import dbm.gnu

import pyinotify


def to_bytes(v):
    return str(v).encode()


def from_bytes(b):
    return int(b.decode())


class DB(pyinotify.ProcessEvent):
    def __init__(self, path):
        self.path = path
        self.callback = None

        wm = pyinotify.WatchManager()
        wm.add_watch(self.path, pyinotify.IN_CLOSE_WRITE)

        self.notifier = pyinotify.ThreadedNotifier(wm, self)
        self.notifier.daemon = True
        self.notifier.start()

    def __del__(self):
        self.notifier.stop()

    def read(self):
        d = {}
        with dbm.open(self.path, "r") as db:
            k = db.firstkey()
            while k is not None:
                d[from_bytes(k)] = from_bytes(db[k])
                k = db.nextkey(k)

        return d

    def delete(self, k):
        with dbm.open(self.path, "w") as db:
            del db[to_bytes(k)]
        if self.callback:
            self.callback()

    def process_IN_CLOSE_WRITE(self, _):
        if self.callback:
            self.callback()
