# 15.10. Эксперименты с библиотеками: попробуйте использовать Matplotlib для создания визуализации бросков кубиков,
# а Plotly — для создания визуализации случайного блуждания. (Для выполнения этого упражнения вам придется обратиться
# к документациям обеих библиотек.)

from random import choice
import plotly.express as px


class RandomWalk:
    """Класс для генерирования случайных блужданий."""
    def __init__(self, points=50):
        self.points = points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.points:
            x = choice([-4, -3, -2, -1, 0, 1, 2, 3, 4])
            y = choice([-4, -3, -2, -1, 0, 1, 2, 3, 4])
            if x == 0 and y == 0:
                continue
            else:
                self.x_values.append(self.x_values[-1] + x)
                self.y_values.append(self.y_values[-1] + y)


# Построение случайного блуждания.
rndw = RandomWalk()
rndw.fill_walk()

x_axis = rndw.x_values
y_axis = rndw.y_values

fig = px.scatter(x=x_axis, y=y_axis,
                 labels={'x': 'Axis X', 'y': 'Axis Y'},
                 )

print(x_axis[:10], y_axis[:10])
fig.show()
