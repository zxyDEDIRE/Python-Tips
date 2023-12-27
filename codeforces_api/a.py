import requests
import datetime
import hashlib

hash = hashlib.sha512()


def get_hash(str):
    hash.update(str.encode('utf-8'))
    return hash.hexdigest()


url = "https://codeforces.com/api/contest.list?gym=false"



ti = datetime.datetime.now()
# url = url + "&apiKey=f3f23facb05c8a33cb36d2bb95e17b089a5f2dbb"
url = url + "&time=" + str(int(ti.timestamp()))
# url = url + "&apiSig=123456"

# st = "123456/contest.list?gym=true?apiKey=f3f23facb05c8a33cb36d2bb95e17b089a5f2dbb&time=" + str(int(ti.timestamp())) + "#abe61a4fac4af497abf6d24f9c0bda6161231b8c"

# url = url + get_hash(st)
print(url)
r = requests.get(url=url)
with open("a.json",'w',encoding='utf-8') as file:
    file.write(r.text)
print(r.text)

"""
contest.list?gym=true
sha512Hex(123456/contest.list?gym=true?apiKey=f3f23facb05c8a33cb36d2bb95e17b089a5f2dbb&time=)
"""
