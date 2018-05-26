import datetime

x = input().split(" ")
for i in range(3):
    x[i] = int(x[i])

data = datetime.date(x[0], x[1], x[2])
data = data + datetime.timedelta(int(input()))


print(data.year, data.month, data.day)
