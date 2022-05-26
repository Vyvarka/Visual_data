import csv
from matplotlib import pyplot as plt
from datetime import datetime


file_1 = 'Visual_data/data/sitka_weather_2018_simple.csv'
file_2 = 'Visual_data/data/death_valley_2018_simple.csv'
with open(file_1) as f1:
    rdr1 = csv.reader(f1)  # объект чтения данных сохраняется в переменной
    header_raw_1 = next(rdr1)  # считываем заголовки
    for i, v in enumerate(header_raw_1):
        print(i, v)

    # Чтение дат и максимальных температур из файла
    lst_prcp_1, dates_1 = [], []
    for x in rdr1:
        current_date = datetime.strptime(x[header_raw_1.index('DATE')], "%Y-%m-%d")
        try:
            lst_prcp_1.append(float(x[header_raw_1.index('PRCP')]))
            dates_1.append(current_date)
        except ValueError:
            print(f'Missing data for {current_date}')

with open(file_2) as f2:
    rdr2 = csv.reader(f2)  # объект чтения данных сохраняется в переменной
    header_raw = next(rdr2)  # считываем заголовки
    for i, v in enumerate(header_raw):
        print(i, v)

    # Чтение дат и максимальных температур из файла
    lst_prcp_2, dates_2 = [], []
    for x in rdr2:
        current_date = datetime.strptime(x[header_raw.index('DATE')], "%Y-%m-%d")
        try:
            lst_prcp_2.append(float(x[header_raw.index('PRCP')]))
            dates_2.append(current_date)
        except ValueError:
            print(f'Missing data for {current_date}')

#1 Missing date 2018-12-13 00:00:00
#1 Missing date 2018-12-14 00:00:00

#2 Missing date 2018-12-01 00:00:00


# Нанесение данных на диаграмму.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates_1, lst_prcp_1, c='blue', linewidth=1)
plt.plot(dates_2, lst_prcp_2, c='orange', linewidth=1)
# plt.fill_between(dates, lst_prcp_1, lst_prcp_2, facecolor='purple', alpha=0.1)

# Форматирование диаграммы.
plt.title("Daily precipitation, 2018\nDeath Valley and Sitka, CA", fontsize=20)
plt.xlabel('Date', fontsize=12)
fig.autofmt_xdate()  # выводит метки дат по диагонали, чтобы они не перекрывались
plt.ylabel("Precipitation (mm)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
# ax.axis([0, 32, 30, 100])  # Назначение диапазона для каждой оси

plt.show()
