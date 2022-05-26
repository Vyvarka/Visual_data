# 15.10. Эксперименты с библиотеками: попробуйте использовать Matplotlib для создания визуализации бросков кубиков,
# а Plotly — для создания визуализации случайного блуждания. (Для выполнения этого упражнения вам придется обратиться
# к документациям обеих библиотек.)


from random import randint
import matplotlib.pyplot as plt


class Die:
    """Класс, представляющий один кубик."""
    def __init__(self, num_sides=6):
        """По умолчанию используется шестигранный кубик."""
        self.num_sides = num_sides
        self.result = self.roll()
        self.frequencies = self.analiz()

    def roll(self, rang=1_000):
        """формируем список результатов бросков. Количество повторений - rang"""
        return list(randint(1, self.num_sides) for x in range(rang))

    def analiz(self):
        """анализируем количество повторений"""
        return list(self.result.count(i) for i in range(1, self.num_sides + 1))


die_1 = Die()
die_2 = Die()
print(die_1.frequencies, die_2.frequencies)

lst_sum = list((die_1.result[x] + die_2.result[x] for x in range(len(die_1.result))))
x = list(set(lst_sum))
y = list(lst_sum.count(i) for i in x)

plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(14, 9))

rects1 = ax.bar(x, y, width=1, edgecolor="white", linewidth=1)

# Назначение заголовка диаграммы и меток осей.
ax.set_title("Result of dice rolls", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Frequency of Result", fontsize=14)

ax.bar_label(rects1, padding=3)
fig.tight_layout()

plt.show()
