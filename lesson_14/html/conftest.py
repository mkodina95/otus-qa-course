
import platform
import sys

import pkg_resources
import pytest
import os


def pytest_addoption(parser):
    parser.addoption("--address", action="store", default="http://192.168.122.244/", help="Opencart web address")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, pytest_html):
    pytest_html = item.config.pluginmanager.getplugin('allure')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        report.extra = extra


@pytest.mark.usefixtures("environment_info")
@pytest.fixture(scope='session', autouse=True)
def configure_html_report_env(request, environment_info):
    request.config._metadata.update(
        {"Browser": request.config.getoption("--browser"),
         "Address": request.config.getoption("--address"),
         "OS Platform": environment_info[0],
         "Machine": environment_info[1],
         "System Path": environment_info[2],
         "Installed Packages": environment_info[3]})
    yield


@pytest.fixture(scope="session")
def environment_info():
    os_platform = platform.platform()
    machine = platform.machine()
    path = os.environ
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
                                      for i in installed_packages])
    return os_platform, machine, path, installed_packages_list


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport():
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        # only add this during call instead of during any stage
        report.test_metadata = 'whatever'
        # edit stage metadata
        report.stage_metadata = {
            'foo': 'bar'
        }
    elif report.when == 'setup':
        report.stage_metadata = {
            'hoof': 'doof'
        }
    elif report.when == 'teardown':
        report.stage_metadata = {
            'herp': 'derp'
        }


def pytest_runtest_setup(item):
    ALL = set("darwin linux win32".split())
    supported_platforms = ALL.intersection(mark.name for mark in item.iter_markers())
    plat = sys.platform
    if supported_platforms and plat not in supported_platforms:
        pytest.skip("cannot run on platform : " + plat)
