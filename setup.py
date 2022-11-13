import os
import shutil
import winshell


def copy_file(filename):
    shutil.copy(os.getcwd() + '\\IKV\\' + filename, 'C:\\IKV\\' + filename)


print('正在配置程序，请稍等！')
if not os.path.exists('C:\\IKV'):
    os.makedirs('C:\\IKV')
for file in os.listdir(os.getcwd() + '\\IKV'):
    copy_file(file)
shortcut = 'C:\\Users\\' + os.getlogin() + '\\AppData\\Roaming\\Microsoft\\Windows\\Start ' \
                                           'Menu\\Programs\\Startup\\IKV.lnk '
winshell.CreateShortcut(
    Path=shortcut, Target='C:\\IKV\\start.bat',
    Icon=('C:\\IKV\\IKV.exe', 0), Description=''
)
os.system('start C:\\IKV\\start.bat')
for file in os.listdir(os.getcwd() + '\\IKV'):
    os.remove(os.getcwd() + '\\IKV\\' + file)
os.rmdir(os.getcwd() + '\\IKV')
print('已经配置完毕！')
