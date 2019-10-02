import pytest
import time


@pytest.fixture(autouse=True, scope='session')
def session_fixture():
    now = time.time()
    print('The tests are running, the current time is {}'.format(time.strftime('%d %b %X', time.localtime(now))))
    yield
    print('The tests have just run, the current time is {}'.format(time.strftime('%d %b %X', time.localtime(now))))


@pytest.fixture(autouse=True, scope='module')
def module_fixture():
    print('This is the module fixture')
    yield
    print('This is the end of the module fixture')


@pytest.fixture()
def some_numbers():
    return 4, 3
