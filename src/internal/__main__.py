import sqlite3


class DatabaseConnection:
    def __init__(self, filename: str):
        self._filename = filename

    def __enter__(self):
        self._db = sqlite3.connect(self._filename)
        return self._db

    def __exit__(self):
        self._db.close()
