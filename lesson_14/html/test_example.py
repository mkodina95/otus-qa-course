import pytest


xfail = pytest.mark.xfail


@pytest.mark.darwin
@pytest.mark.required
def test_example1():
    pass


@pytest.mark.required
def test_example2():
    assert 1 == 2


@pytest.mark.win32
@pytest.mark.optional
def test_example3():
    assert 1 == 2


@pytest.mark.linux
@pytest.mark.optional
def test_example4():
    assert 2 == 2


@pytest.mark.darwin
@pytest.mark.skip(reason="obsolete")
def test_optional():
    assert 1 == 2


@pytest.mark.darwin
@xfail(reason="not implemented")
def test_not_working():
    assert 0
