import os
import sys
import time


os.chdir('/opt/python-telegram)
with open('config.txt') as f:
  lines=f.read().splitlines()
  for count,line in enumerate(lines,1):
    if line[0]=='#':
      continue
    list=line.split()
    #print(list)
    apiid=list[0]
    apihash=list[1]
    phone=list[2]
    chatid=list[3]
    text=list[4]
    print('%s=====%s====='%('' if count==1 else '\n',count))
    if len(sys.argv)>1 and sys.argv[1]=='check':
      os.system("python3 examples/chat_stat.py %s %s '%s' %s"%(apiid,apihash,phone,chatid))
    else:
      os.system("python3 examples/send_message.py %s %s '%s' %s '%s'"%(apiid,apihash,phone,chatid,text))
    time.sleep(10)
