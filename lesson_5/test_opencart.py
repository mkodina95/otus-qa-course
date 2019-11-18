def test_open_mainpage(open_browser, url_param):
    """
The test checks if the opened page has the necessary url
    """
    open_browser.get(url_param)
    assert open_browser.current_url == url_param
    open_browser.close()
