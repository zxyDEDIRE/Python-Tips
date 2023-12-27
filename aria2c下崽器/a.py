import os
import subprocess


# # order = 'config --referer="https://pixivic.com" -d C:/Users/tob/Desktop/CESHI/ -o a.jpg https://o.acgpic.net/img-original/img/2023/03/27/19/25/53/106614132_p0.jpg'
# order = 'C:/Users/tob/Desktop/作业/自己写的小程序/aria2-1.36.0-win-64bit-build1/config.exe --referer="https://pixivic.com" -d C:/Users/tob/Desktop/CESHI/ -o a.jpg https://o.acgpic.net/img-original/img/2023/03/27/19/25/53/106614132_p0.jpg'
# # order = 'config -d C:/Users/tob/Desktop/CESHI/ https://www.bilibili.com/'
# os.system(order)



url = "https://o.acgpic.net/img-original/img/2023/03/27/19/25/53/106614132_p0.jpg"
referer = 'https://pixivic.com'
header = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'
s_path = 'C:/Users/tob/Desktop/作业/自己写的小程序/Bilibili-1.5.7/aria2c.exe'
t_path = 'C:/Users/tob/Desktop/CESHI/'
command = [s_path,'-d',t_path, '--refer', referer, '--header',header,url]
print(command)
subprocess.call(command)
"""
C:/Users/tob/Desktop/作业/自己写的小程序/Bilibili-1.5.7/config.exe
config --referer="https://pixivic.com" https://o.acgpic.net/img-original/img/2023/03/27/19/25/53/106614132_p0.jpg
C:/Users/tob/Desktop/作业/自己写的小程序/aria2-1.36.0-win-64bit-build1/config.exe --referer="https://pixivic.com" -d C:/Users/tob/Desktop/CESHI/ -o a.jpg https://o.acgpic.net/img-original/img/2023/03/27/19/25/53/106614132_p0.jpg
"""


"""
下载命令：config htts://bilibili.com
-o <下载文件的名字>
--referer=<>
--herder=<>
-d <下载到的路径>
"""

