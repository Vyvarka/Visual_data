import matplotlib.pyplot as plt
from random import choice


# 15.3. Молекулярное движение: измените программу rw_visual.py и замените plt.scatter() вызовом plt.plot().
# Чтобы смоделировать путь пыльцевого зерна на поверхности водяной капли, передайте значения rw.x_values и rw.y_values
# и включите аргумент linewidth. Используйте 5000 точек вместо 50 000.

class RandomWalk:
    """Класс для генерирования случайных блужданий."""
    def __init__(self, points=5000):
        self.points = points
        self.x_values = [0]
        self.y_values = [0]

    # выполнения задания 15.5
    def get_step(self):
        self.step = choice(list(x for x in range(-4, 5) if x != 0))
        return self.step
        # для выполнения задания 15.4 устанавливаем диапазон 0, 8

    def fill_walk(self):
        while len(self.x_values) < self.points:
            x_step = self.get_step()
            self.x_values.append(self.x_values[-1] + x_step)
            y_step = self.get_step()
            self.y_values.append(self.y_values[-1] + y_step)


# Построение случайного блуждания.
rndw = RandomWalk()
rndw.fill_walk()

# Нанесение точек на диаграмму.
fig, ax = plt.subplots(figsize=(15, 9))  # figsize получает кортеж с размерами окна диаграммы в дюймах
ax.plot(rndw.x_values, rndw.y_values, linewidth=1)
# выделяем вторую точку синим цветом
ax.scatter(rndw.x_values[0], rndw.y_values[0], s=20, c='orange', edgecolors='none')
# выделяем последнюю точку красным цветом
ax.scatter(rndw.x_values[-1], rndw.y_values[-1], s=20, c='red', edgecolors='none')
ax.set_title("Random Walk", fontsize=14)
"""
ax.set_xlabel("Value_X", fontsize=10)
ax.set_ylabel("Value_Y", fontsize=10)
"""

# Удаление осей
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()






