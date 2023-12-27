import datetime

begin = datetime.date(2023,1,1)
end = datetime.date.today()
d = begin
delte = datetime.timedelta(days=1)
while d <= end:
    print(str(d))
    d += delte
