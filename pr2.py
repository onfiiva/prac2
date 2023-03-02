from calendar import Calendar
year = int(input("Введите год \n"))
days = Calendar()
summ = 0
for month in range(1,13):
    lis = days.itermonthdays(year, month)
    for i in lis:
        if (i // 10 > 0):
            summ += i%10
            summ += i//10
        else:
            summ += i
print(summ)