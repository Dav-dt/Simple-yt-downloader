import os

def getDesktopPath()->str:
    """
    Function which returns the desktop path of the user
    """
    return os.path.join(os.path.expanduser('~'), 'Desktop')


def makeDefaultOutPutDir()->str:
    """
    Function to create a dir
    """
    if not os.path.exists(getDesktopPath() + r"\YT-DlOutput"):
        os.mkdir(getDesktopPath() + r"\YT-DlOutput")

    return os.path.join(getDesktopPath() + r"\YT-DlOutput")

def sendToGithubPage()->None:
    """
    About button.
    """
    from webbrowser import open
    open("https://github.com/Dav-dt")

    return None