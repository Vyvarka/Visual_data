import requests
from plotly.graph_objs import Bar
from plotly import offline


# Создание вызова API и сохранение ответа.
url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Сохранение ответа API в переменной.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Анализ информации о репозиториях.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Обработка результатов.
# print(response_dict.keys())

# Анализ первого репозитория: сколько содержит ключей
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")

repo_links, stars, labels = [], [], []

for i in repo_dicts:
    repo_name = i['name']
    repo_url = i['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(i['stargazers_count'])

    owner = i['owner']['login']
    description = i['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {'color': 'rgb(250,0,0)', 'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}},
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Java Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {'title': 'Repository', 'titlefont': {'size': 24}, 'tickfont': {'size': 14}},
    'yaxis': {'title': 'Stars', 'titlefont': {'size': 24}, 'tickfont': {'size': 14}},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='java_repos.html')
