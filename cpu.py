# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:52:45 2023

@author: Nazanin Shahmiri
"""

import schedule
import psutil
import os
from slacker import Slacker
import datetime
import time
import json
import requests

cpu_threshold= 80
logfile='/var/log/monitor.log'

io = psutil.cpu_times_percent().iowait
cpu = psutil.cpu_percent(interval=1)
#print(f'cpu usage : {cpu}% | I/O wait : {io}%')
cpu_dic = { "cpu": cpu , "io":io }
print(cpu_dic)


slack_data1 = {
            "username": "NOC-Bot",
            "icon_emoji": ":bulb:",
            "channel": 'nazanin_test2',
            "text": 'CPU usage is currently above %s percent' % cpu_threshold,
            "attachments": [
                {
                    "color": "#E51A4C",
                    "fields": [
                        {
                            "title": 'CPU ALERT',
                            "value": f'io is {io} | cpu is {cpu}',
                            "short": "false",
                        }
                    ]
                }
            ]
        }

slack_data2 = {
            "username": "NOC-Bot",
            "icon_emoji": ":bulb:",
            "channel": 'nazanin_test2',
            "text": f'io is {io} | cpu is {cpu}' ,
            "attachments": [
                {
                    "color": "#E51A4C",
                    "fields": [
                        {
                            "title": 'CPU ALERT',
                            "value": 'CPU usage is currently below %s percent' % cpu_threshold ,
                            "short": "false",
                        }
                    ]
                }
            ]
        }
webhook_url = 'https://hooks.slack.com/services/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'
headers = {
        'Content-Type': "application/json",
    }

if cpu  > cpu_threshold:
     print (time.strftime("%c") + ' - CPU ALERT - CPU usage is currently above %s percent' % cpu_threshold)
     with open(logfile, 'a') as file_handle:
         file_handle.write(time.strftime("%c") + ' - CPU ALERT - CPU usage is currently above %s percent' % cpu_threshold)
         response = requests.post( webhook_url,
                 data=json.dumps(slack_data1),
                 headers=headers
             )
else:
      #slack.chat.post_message('nazanin_test', 'CPU usage is below %s' % cpu_threshold)
      print (time.strftime("%c") + ' - cpu is below %s percent' % cpu_threshold)
      with open(logfile, 'a') as file_handle:
          file_handle.write(time.strftime("%c") + ' - cpu is below %s percent' % cpu_threshold)
          response = requests.post( webhook_url,
                  data=json.dumps(slack_data2),
                  headers=headers
              )



