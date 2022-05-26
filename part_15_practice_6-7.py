# 15.6. Два кубика D8: создайте модель, которая показывает, что происходит при 1000-кратном бросании двух восьмигранных
# кубиков. Попробуйте заранее представить, как будет выглядеть визуализация, перед моделированием; проверьте
# правильность своих интуитивных представлений. Постепенно наращивайте количество бросков, пока не начнете замечать
# ограничения, связанные с ресурсами вашей системы.
# 15.7. Три кубика: при броске трех кубиков D6 наименьший возможный результат равен 3, а наибольший — 18. Создайте
# визуализацию, которая показывает, что происходит при броске трех кубиков D6.


from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Die:
    """Класс, представляющий один кубик."""
    def __init__(self, num_sides=8):
        """По умолчанию используется восьмигранный кубик."""
        self.num_sides = num_sides
        self.result = self.roll()
        self.frequencies = self.analiz()

    def roll(self, rang=10_000):
        """формируем список результатов бросков. Количество повторений - rang"""
        return list(randint(1, self.num_sides) for x in range(rang))

    def analiz(self):
        """анализируем количество повторений"""
        return list(self.result.count(i) for i in range(1, self.num_sides + 1))

"""
# __________________________решение задачи 15.6_________________________
die_1 = Die()
die_2 = Die()
print(die_1.frequencies, die_2.frequencies)

x_values = list(range(2, die_1.num_sides + die_2.num_sides + 1))
sum_values = list(die_1.result[i] + die_2.result[i] for i in range(len(die_1.result)))
y_values = list(sum_values.count(x) for x in x_values)
data = [Bar(x=x_values, y=y_values)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling two D8 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')
"""

# ________________________________решение задачи 15.7_________________________________
die_1 = Die(6)
die_2 = Die(6)
die_3 = Die(6)
print(die_1.frequencies, die_2.frequencies, die_3.frequencies)

x_values = list(range(3, die_1.num_sides + die_2.num_sides + die_3.num_sides + 1))
sum_values = list(die_1.result[i] + die_2.result[i] + die_3.result[i] for i in range(len(die_1.result)))
y_values = list(sum_values.count(x) for x in x_values)
data = [Bar(x=x_values, y=y_values)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling three D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')
