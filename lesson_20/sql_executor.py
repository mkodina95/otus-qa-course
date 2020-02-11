class SqlExecutor(object):
    def __init__(self, sql_connector):
        self.sql_connector = sql_connector.get_connector()

        if self.sql_connector is None:
            self.cursor = None
        else:
            self.cursor = self.sql_connector.cursor()

    def get_one_result(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchone()
        except Exception:
            return None

    def get_all_result(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception:
            return None

    def exec_edit_query(self, query):
        try:
            self.cursor.execute(query)
            self.sql_connector.commit()
            return True
        except Exception:
            return False

    def close(self):
        self.cursor.close()
        self.sql_connector.close()






