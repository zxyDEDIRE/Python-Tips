



import json
import os
import subprocess
import datetime
import time


Mem = dict()

def ReadMem():
    F = open('Mem.json', 'r', encoding='utf-8')
    content = F.read()
    F.close()
    return json.loads(content)

def WriteMem(mp):
    now_mem = json.dumps(mp)
    F2 = open('Mem.json', 'w+')
    F2.write(now_mem)
    F2.close()

def down(title, cnt, url, path):
    header = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'
    referer = 'https://pixivic.com'
    s_path = Mem['aria2c_exe']
    path = path + '/'
    name = title + '_' + str(cnt) + '.jpg'
    if name in Mem['data'].keys():
        return
    command = [s_path, '-d', path, '-o', name, '--refer', referer, '--header', header, url]
    subprocess.call(command)
    Mem['data'][name] = True
    WriteMem(Mem)
