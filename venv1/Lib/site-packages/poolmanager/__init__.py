# -*- coding: utf-8 -*-

import time
import multiprocessing


class KeyboardInterruptError(Exception):
    pass


class PoolManager:

    def __init__(self, numProcs=multiprocessing.cpu_count(), factor=1,
                 store=False):
        self._numProcs = int(numProcs * factor)
        self._pool = multiprocessing.Pool(
            self._numProcs
        )
        self._store = store
        self._counter = 0
        self.results = []

    def _abort(self):
        self._pool.terminate()
        self._pool.join()

    def _writer(self, records, callback):
        for r in records:
            self._counter += 1
            if self._store:
                self.results.append(r)
            if hasattr(callback, '__call__'):
                callback(self._counter, r)

    def _create(self, func):
        try:
            return func
        except KeyboardInterrupt:
            raise KeyboardInterruptError()
        except Exception as e:
            raise Exception(e)

    def imap_unordered(self, func, iterable, chunks, callback=None):
        try:
            self._writer(self._pool.imap_unordered(
                self._create(func), iterable, chunks
            ), callback)
            self._pool.close()
            while self.nbOfProcessesAlive > 0:
                time.sleep(2)

            self._pool.join()
        except KeyboardInterruptError:
            self._abort()
        except Exception as e:
            self._abort()
            raise Exception(e)

    @property
    def nbOfProcesses(self):
        return self._numProcs

    @property
    def nbOfProcessesAlive(self):
        return len([p for p in self._pool._pool if p.is_alive()])
