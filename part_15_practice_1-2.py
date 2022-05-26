import matplotlib.pyplot as plt

#  15.1. число, возведенное в третью степень, называется «кубом». Нанесите на диаграмму первые пять кубов, а затем
#  первые 5000 кубов.
#  15.2. Цветные кубы: примените цветовую карту к диаграмме с кубами

x_values = list(range(1, 20))  # при необходимости меняем значение на 5001
y_values = [i**3 for i in x_values]

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=2, c=y_values, cmap=plt.cm.Greys)
ax.scatter(x_values[::3], y_values[::3], s=20, c='red')

ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax .set_ylabel("Cube of Value", fontsize=14)

plt.show()
