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
    sitka_tmax, sitka_tmin, dates_1 = [], [], []
    for x in rdr1:
        current_date = datetime.strptime(x[header_raw_1.index('DATE')], "%Y-%m-%d")
        try:
            sitka_tmax.append(float(x[header_raw_1.index('TMAX')]))
            sitka_tmin.append(float(x[header_raw_1.index('TMIN')]))
            dates_1.append(current_date)
        except ValueError:
            print(f'Missing data for {current_date}')
    name_1 = x[header_raw_1.index('NAME')]

with open(file_2) as f2:
    rdr2 = csv.reader(f2)  # объект чтения данных сохраняется в переменной
    header_raw = next(rdr2)  # считываем заголовки
    for i, v in enumerate(header_raw):
        print(i, v)

    # Чтение дат и максимальных температур из файла
    dv_tmax, dv_tmin, dates_2 = [], [], []
    for x in rdr2:
        current_date = datetime.strptime(x[header_raw.index('DATE')], "%Y-%m-%d")
        try:
            dv_tmax.append(float(x[header_raw.index('TMAX')]))
            dv_tmin.append(float(x[header_raw.index('TMIN')]))
            dates_2.append(current_date)
        except ValueError:
            print(f'Missing data for {current_date}')
    name_2 = x[header_raw.index('NAME')]


# Нанесение данных на диаграмму.
plt.style.use('seaborn')
fig, ax = plt.subplots()

# создаем диапазон для Sitka
ax.plot(dates_1, sitka_tmax, c='red', linewidth=1, alpha=0.5)
plt.plot(dates_1, sitka_tmin, c='blue', linewidth=1, alpha=0.5)
plt.fill_between(dates_1, sitka_tmax, sitka_tmin, facecolor='blue', alpha=0.1)

# создаем диапазон для Death_valley
plt.plot(dates_2, dv_tmax, c='orange', linewidth=1, alpha=0.5)
plt.plot(dates_2, dv_tmin, c='purple', linewidth=1, alpha=0.5)
plt.fill_between(dates_2, dv_tmax, dv_tmin, facecolor='purple', alpha=0.1)

# Форматирование диаграммы.
plt.title(f"Daily high and low temperatures, 2018"
          f"\n{name_1} and "
          f"{name_2}", fontsize=20)
plt.xlabel('Date', fontsize=12)
fig.autofmt_xdate()  # выводит метки дат по диагонали, чтобы они не перекрывались
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
ax.axis([dates_1[0], dates_1[-1], 0, 140])  # Назначение диапазона для каждой оси

plt.show()
