class CheckExistenceDB(object):
    def __init__(self, executor):
        self.executor = executor

    def check_exist(self):
        result = self.executor.get_all_result("select * from oc_cart")
        assert result is not None and len(result) > 0

    def check_is_not_exist(self):
        result = self.executor.get_all_result("select * from oc_cart")
        assert result is None or len(result) == 0
