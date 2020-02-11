import datetime


class DBLogging(object):
    def __init__(self, db_executor):
        self.db_executor = db_executor
        # preinit, create table
        self.db_executor.exec_edit_query("""
             create table logs (log_id integer primary key AUTOINCREMENT,
                                date varchar,
                                type varchar,
                                msg varchar)
         """)

    def log(self, log_type, msg):
        now_date = datetime.datetime.now()
        sql_query = f"insert into logs (date, type, msg) values(\"{now_date}\", \"{log_type}\", \"{msg}\")"
        self.db_executor.exec_edit_query(sql_query)

    def print_logs(self):
        result = self.db_executor.get_one_result("select * from logs")
        print(result)

