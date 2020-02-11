import pymysql


class MySqlConnector(object):
    def __init__(self, host: str, user: str, db: str):
        self.connection = pymysql.connect(host=host, user=user, db=db)

    def get_connector(self):
        return self.connection
