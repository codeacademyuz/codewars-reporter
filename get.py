import requests
import csv

URL = 'http://127.0.0.1:8000/'
URL = 'https://codeschoolhomeworkapi.pythonanywhere.com/'

def get_group_results_daily(group: str):
    response = requests.get(f"{URL}codewars/group/{group}")
    data = response.json()['data']
    results = [['name', 'daily']]
    for s in data:
        name, total = list(s.items())[0]
        results.append([name, total])

    with open(f'client/codewars/{group}-daily.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(results)

def get_group_results_all(group: str):
    response = requests.get(f"{URL}codewars/group-all/{group}")
    problems = response.json()['problems']
    results = [['name', 'total']]
    for s in problems:
        name, total = list(s.items())[0]
        results.append([name, total])


    with open(f'client/codewars/{group}-all.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(results)


# get_group_results_all('CODEWARS_2022A')
# get_group_results_daily('CODEWARS_2022A')
codewars = ['yusupovna1403',
'smartboy0310',
'Muxi86',
'farhod-rozikov',
'BilolMuhammad',
'bahte',
'AzimUlmasov']

# https://codeschoolhomeworkapi.pythonanywhere.com/codewars/group-all/CodeWars-2023A
group = 'CodeWars-2023A'
get_group_results_daily(group)
get_group_results_all(group)
