import pyautogui


class Rec:
    def __init__(self, filename='img.jpg', **kwargs):
        self.filename = filename

    def start(self):
        while True:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(f'{self.filename}')
