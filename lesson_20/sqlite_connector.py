import sqlite3


class SqliteConnector(object):
    def __init__(self, configuration):
        self.connection = sqlite3.connect(configuration)

    def get_connector(self):
        return self.connection