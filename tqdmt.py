import tqdm
from threading import Thread
from multiprocessing import Queue


class tqdmt:
    def __init__(self, total: int, n: int = None):
        self.pb = tqdm.tqdm(total=total, position=n)
        self._q = Queue()
        self._thread = Thread(target=lambda: self._bg_run())

    def start(self):
        self._thread.start()

    def process_done(self):
        self._q.put(1)

    def done(self):
        self._q.put(None)
        self.pb.close()

    @property
    def total(self):
        return self.pb.total

    @total.setter
    def total(self, new):
        self.pb.total = new

    def _bg_run(self):
        while self._q.get() is not None:
            self.pb.update()