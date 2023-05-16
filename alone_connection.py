import time

import pysftp
#
from Config.config import login_data
import subprocess
import datetime
#
# def connection(username, ip, password):
#      try:
#          connect = 'putty.exe -ssh {}@{} -pw {}'.format(username, ip, password)
#          subprocess.Popen(connect, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#      except:
#          print("Connection Failed...\nCheck your credentials access...")
#
#  # connection super user
# #connection('itmx16', login_data.ip, "sgeg4913")
# connection('itmx12', login_data.ip, "sgem5986")#serch
#
#

import os
import pyautogui as pa
# os.system('start cmd')


def sftp_connection(host, username, password):
    try:  # -ssh
        os.system(f'start cmd /c psftp')
        time.sleep(2)
        pa.typewrite(f'open {host}')
        pa.press("enter")
        pa.typewrite(f'{username}')
        pa.press("enter")
        pa.typewrite(f'{password}')
        pa.press("enter")

    except:
        print("Connection Failed...\nCheck your credentials access...")


sftp_connection('192.168.1.3', 'itmx12', 'sgem5986')

# # connection test user
# for i in range(15):
#
#     print(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M:%S.%f/"))
#     #connection(login_data.linux_username, login_data.ip, login_data.password)
#     #connection("itmx17", login_data.ip, "java135")
#     #connection("test18", login_data.ip, "123abc")
#     connection("test78", login_data.ip, "verastream")
#     #connection(login_data.linux_username, login_data.ip, login_data.password)
#     #time.sleep(2)
# print(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M:%S.%f/"))

