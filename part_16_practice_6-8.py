import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Изучение структуры данных.
filename = 'Visual_data/data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

title = all_eq_data['metadata']['title']
all_eq_dicts = all_eq_data['features']
mags, lons, lats, places = [], [], [], []
for i in all_eq_dicts:
    mags.append(i['properties']['mag'])
    lons.append(i['geometry']['coordinates'][0])
    lats.append(i['geometry']['coordinates'][1])
    places.append(i['properties']['place'])

print(len(mags))

# Нанесение данных на карту.
data = [Scattergeo(lon=lons, lat=lats,
                   marker={'size': [5*mag for mag in mags], 'color': mags,
                           'colorscale': [[0, 'rgb(255,255,0)'], [1, 'rgb(255,0,0)']],
                           'colorbar': {'title': 'Magnitude'},
                           'reversescale': False},
                   text=places
                   )]

my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
