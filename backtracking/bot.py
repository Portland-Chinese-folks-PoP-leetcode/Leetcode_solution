import time
import pyautogui as pg
import pyperclip as pc


class SendMsg(object):

    def __init__(self):
        self.name = '文件传输助手'
        self.msg = '自动发微信消息'

    def send_msg(self):
        # 操作间隔为1秒
        pg.PAUSE = 1.5
        pg.hotkey('ctrl', 'alt', 'w')
        pg.hotkey('ctrl', 'f')

        # 找到好友
        pc.copy(self.name)
        pg.hotkey('ctrl', 'v')
        pg.press('enter')

        # 发送消息
        pc.copy(self.msg)
        pg.hotkey('ctrl', 'v')
        pg.press('enter')

        # 隐藏微信
        time.sleep(1)
        pg.hotkey('ctrl', 'alt', 'w')


if __name__ == '__main__':
    s = SendMsg()
    while True:
        s.send_msg()
