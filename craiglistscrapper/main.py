import requests
from bs4 import BeautifulSoup

data = requests.get('https://newyork.craigslist.org/d/software-qa-dba-etc/search/sof')

soup = BeautifulSoup(data.text, 'html.parser')


job_title = []
job_url = []

for ul in soup.find_all('ul'):
    for li in ul.find_all('li'):
        values = [a.text for a in li.find_all('a', {'class': 'result-title hdrlnk'})]
        job_title.append(values)


for ul in soup.find_all('ul'):
    for li in ul.find_all('li'):
        for link in li.find_all('a'):
            values = [link.get('href')]
            job_url.append(values)

print(job_title)
print(job_url)
