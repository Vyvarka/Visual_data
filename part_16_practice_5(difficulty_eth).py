import csv
from matplotlib import pyplot as plt
from datetime import datetime


file_1 = 'Visual_data/data/eth.csv'
with open(file_1) as f1:
    rdr1 = csv.reader(f1)  # объект чтения данных сохраняется в переменной
    header_raw = next(rdr1)  # считываем заголовки
    for i, v in enumerate(header_raw):
        print(i, v)

    # Чтение дат и максимальных температур из файла
    lst_values, dates = [], []

    for x in rdr1:
        current_date = datetime.strptime(x[header_raw.index('Date(UTC)')], "%m/%d/%Y")
        try:
            lst_values.append(float(x[header_raw.index('Value')]))
            dates.append(current_date)
        except ValueError:
            print(f'Missing data for {current_date}')


# Нанесение данных на диаграмму.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, lst_values, c='blue', linewidth=1, alpha=0.5)
plt.plot(dates, [0]*len(lst_values), c='gray', linewidth=1, alpha=0.5)
plt.fill_between(dates, lst_values, [0]*len(lst_values), facecolor='blue', alpha=0.2)

# Форматирование диаграммы.
plt.title("Ethereum network difficulty chart", fontsize=20)
plt.xlabel('Date', fontsize=12)
fig.autofmt_xdate()  # выводит метки дат по диагонали, чтобы они не перекрывались
plt.ylabel("Difficulty (TH)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
# ax.axis([0, 32, 30, 100])  # Назначение диапазона для каждой оси

plt.show()
