import os 
import sys
import time

# get current working directory
# cwd = os.getcwd()

# print cwd
# print(cwd)

# create a new dictionary with dummy data
data = {'id': 100, 'age': 25, 'insurance': 0}

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open('/home/mengyao/crontab/testFile_' + nowStr + '.txt', 'w') as f:
    f.write(str(data))