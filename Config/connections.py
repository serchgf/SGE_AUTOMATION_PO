import time
import os
import pyautogui as pa
from Config.config import login_data
import subprocess
import datetime

class ssh_putty_connection:

    def sge_connection(self, username, ip, password):
        try:
            connect = 'putty.exe -ssh {}@{} -pw {}'.format(username, ip, password)
            subprocess.Popen(connect, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        except:
            print("Connection Failed...\nCheck your credentials access...")




# os.system('start cmd')

class sftp_connection:
    def sftp_connection(self, host, username, password):
            os.system(f'start cmd /c psftp')
            time.sleep(2)
            pa.typewrite(f'open {host}')
            pa.press("enter")
            pa.typewrite(f'{username}')
            pa.press("enter")
            pa.typewrite(f'{password}')
            pa.press("enter")
            time.sleep(2)
#sftp_connection('192.168.1.3', 'itmx12', 'sgem5986')


