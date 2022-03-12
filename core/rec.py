import pyautogui


class Rec:
    def __init__(self, filename='img.jpg', **kwargs):
        self.filename = filename
        self.stop = False

    def start(self):
        while True:
            self.update()
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(f'{self.filename}')


    def update(self):
        if self.stop:
            print('stopped')
            exit()