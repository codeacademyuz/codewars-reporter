import requests
from datetime import datetime


def daily(user) -> int:
    URL = f'https://www.codewars.com/api/v1/users/{user}/code-challenges/completed'
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()

        count = 0
        for CompletedChallenge in data['data']:
            date = datetime.fromisoformat(CompletedChallenge['completedAt'])

            now = datetime.now()

            if date.day == now.day:
                count += 1

        return count
    
    else:
        return 0

print(daily('djumanov'))