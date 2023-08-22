import time
import pytest


@pytest.fixture(autouse=True, scope='module')
def time_after_module_tests():
    yield 
    print("module finished. not time...")
    
    
@pytest.fixture(autouse=True, scope='class')
def time_after_class_tests():
    yield 
    now = time.time()
    print("---")
    print("each class finished: {}".format(time.strftime('%d %b %X', time.localtime(now))))
    print("------------")


@pytest.fixture(autouse=True, scope='function')
def time_after_each_test():
    yield
    now = time.time()
    print("---")
    print("each class finished: {}".format(time.strftime('%d %b %X', time.localtime(now))))
    print("------------")


@pytest.fixture()
def number_42():
    return 42
