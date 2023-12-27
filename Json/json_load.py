import json


def ReadJS():
    F = open('Mem.json', 'r')
    content = F.read()
    F.close()
    return json.loads(content)


def WriteJS(mp):
    now_mem = json.dumps(mp)
    F2 = open('Mem.json', 'w+')
    F2.write(now_mem)
    F2.close()