import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# 0 latitude
# 1 longitude
# 2 brightness
# 3 scan
# 4 track
# 5 acq_date
# 6 acq_time
# 7 satellite
# 8 confidence
# 9 version
# 10 bright_t31
# 11 frp
# 12 daynight

file_1 = 'Visual_data/data/world_fires_1_day.csv'
with open(file_1) as f1:
    rdr1 = csv.reader(f1)  # объект чтения данных сохраняется в переменной
    header_raw_1 = next(rdr1)  # считываем заголовки
    """
    for i, v in enumerate(header_raw_1):  # выводим название заголовков
        print(i, v)
    """
    # Чтение из файла. Создание списков координат, площади пожара и его силы
    lst_s, lons, lats, lst_frp = [], [], [], []
    for x in rdr1:
        try:
            lats.append(float(x[header_raw_1.index('latitude')]))
            lons.append(float(x[header_raw_1.index('longitude')]))
            lst_s.append(float(x[header_raw_1.index('brightness')]))
            lst_frp.append(float(x[header_raw_1.index('frp')]))
        except ValueError:
            print(f'Missing data')

title = 'Global fires, 1 days'
print(len(lons))  # необходимо для понимания объема данных

# Нанесение данных на карту.
data = [Scattergeo(lon=lons[:5000], lat=lats[:5000],
                   marker={'size': [x/20 for x in lst_s[:5000]], 'color': lst_s[:5000],
                           'colorscale': [[0, 'rgb(255,255,0)'], [1, 'rgb(255,0,0)']],
                           'colorbar': {'title': 'level fires'},
                           'reversescale': False}, text=lst_frp[:5000]
                   )]

my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')
