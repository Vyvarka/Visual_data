# 15.8. Умножение: при броске двух кубиков результат обычно определяется суммированием двух чисел. Создайте
# визуализацию, которая показывает, что происходит при умножении этих чисел.
# 15.9. Генераторы: для наглядности в списках этого раздела используется длинная форма цикла for. Если вы уверенно
# работаете с генераторами списков, попробуйте написать генератор для одного или обоих циклов в каждой из этих программ

from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Die:
    """Класс, представляющий один кубик."""
    def __init__(self, num_sides=6):
        """По умолчанию используется шестигранный кубик"""
        self.num_sides = num_sides
        self.result = self.roll()
        self.frequencies = self.analiz()

    def roll(self, rang=10_000):
        """формируем список результатов бросков. Количество повторений - rang"""
        return list(randint(1, self.num_sides) for x in range(rang))

    def analiz(self):
        """анализируем количество повторений"""
        return list(self.result.count(i) for i in range(1, self.num_sides + 1))


# __________________________решение задачи 15.8_________________________
die_1 = Die()
die_2 = Die()
print(die_1.frequencies, die_2.frequencies)
# создаем список результатов произведений двух шестигранных кубиков
sum_values = list(die_1.result[i] * die_2.result[i] for i in range(len(die_1.result)))
# определяем оси координат для нанесения значений
x_values = list(set(sum_values))
y_values = list(sum_values.count(x) for x in x_values)
data = [Bar(x=x_values, y=y_values)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling two D6 10000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='mult_d6_d6.html')
