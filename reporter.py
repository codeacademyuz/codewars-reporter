import requests
from datetime import datetime
import csv


def daily(user) -> int:
    URL = f'https://www.codewars.com/api/v1/users/{user}/code-challenges/completed'
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()

        now = datetime.now()
        count = 0
        for CompletedChallenge in data['data']:
            date = datetime.fromisoformat(CompletedChallenge['completedAt'])

            d = (now - date.replace(tzinfo=None))

            if d.total_seconds() <= 86400:
                count += 1

        return count
    
    else:
        return 0


def daily_report_by_group(file_name):
    report = [['first name', 'last name', 'total']]
    with open(file_name) as csv_file:
        dict_reader = csv.DictReader(csv_file)

        for user in dict_reader:
            count = daily(user['username'])
            report.append([user['first name'], user['last name'], count])

    with open(f"daily - {file_name}", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(report)

file_name = 'A.csv'
print(daily('djumanov'))