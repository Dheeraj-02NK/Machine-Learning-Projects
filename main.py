import os
from random import randint
from datetime import datetime, timedelta

start_date = datetime(2023, 8, 12)
end_date = datetime(2023, 12, 16)

current_date = start_date

while current_date <= end_date:
    num_commits = randint(1, 10)

    for _ in range(num_commits):
        d = current_date.strftime("%Y-%m-%d %H:%M:%S")
        with open('file1.txt', 'a') as file:
            file.write(d + '\n')
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "random commit"')

    current_date += timedelta(days=1)

os.system('git push -u origin main')
