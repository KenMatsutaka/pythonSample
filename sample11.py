# calendar : カレンダーを扱うライブラリ
import calendar

# 月末を表示
print(calendar.monthrange(2020,1)[1])
print(calendar.monthrange(2020,2)[1])

# 年月を指定してカレンダーを表示
calendar.prmonth(2020,2)

# 起点になる曜日を指定してカレンダー表示
c = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2020,5)

# うるう年判定
print(calendar.isleap(2019))
print(calendar.isleap(2020))