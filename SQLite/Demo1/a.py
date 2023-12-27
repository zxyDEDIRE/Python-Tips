import sqlite3

con = sqlite3.connect("demo1.db")
cur = con.cursor()
# sql_text_1 = '''CREATE TABLE scores
#            (姓名 TEXT,
#             班级 TEXT,
#             性别 TEXT,
#             语文 NUMBER,
#             数学 NUMBER,
#             英语 NUMBER);'''
# cur.execute(sql_text_1)
sql_text_2 = "INSERT INTO scores VALUES('A', '一班', '男', 96, 94, 98)"
cur.execute(sql_text_2)
con.commit()