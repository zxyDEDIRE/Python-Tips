import datetime



# 时间戳 转 <class 'datetime.datetime'>
ti = 1690002000
_ti = datetime.datetime.fromtimestamp(ti)

# <class 'datetime.datetime'> 转 str
new_str = _ti.strftime("%Y-%m-%d %H:%M:%S")
print(new_str)

# str 转 <class 'datetime.datetime'>
_new_ti = datetime.datetime.strptime(new_str, "%Y-%m-%d %H:%M:%S")
print(type(_new_ti))

# <class 'datetime.datetime'> 转 时间戳
fl = _new_ti.timestamp()

# 创建表示五个小时时间间隔的 timedelta 对象
time_delta = datetime.timedelta(hours=5)

# 将时间间隔对象加上 datetime 对象
new_time = _new_ti + time_delta

# 将结果转换回字符串格式
new_time_str = new_time.strftime("%Y-%m-%d %H:%M:%S")

# 获取当前时间
_a = datetime.datetime.now()