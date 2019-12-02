from lesson_8.action_chains import DragAndDropActionChain


def test_move_to_trash(open_browser, trash_url):
    """ The test moves all the documents to trash"""
    open_browser.get(trash_url)
    DragAndDropActionChain.drag_and_drop_to_trash(open_browser)
    open_browser.close()
