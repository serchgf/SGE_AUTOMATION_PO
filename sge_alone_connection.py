import time

import pysftp
#
from Config.config import login_data
import subprocess
import datetime
#
def connection(username, ip, password):
     try:
         connect = 'putty.exe -ssh {}@{} -pw {}'.format(username, ip, password)
         subprocess.Popen(connect, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
     except:
         print("Connection Failed...\nCheck your credentials access...")

 # connection super user
#connection('itmx16', login_data.ip, "sgeg4913")
connection('itmx12', login_data.ip, "sgem5986")#serch
#connection('itmx11', login_data.ip, "sgem5986")#serch2

