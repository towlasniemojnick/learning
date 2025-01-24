import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_cards = results.find_all("div", class_="card-content")

for jc in job_cards:
    title_el = jc.find("h2", class_="title")
    company_el = jc.find("h3", class_="company")
    loc_el = jc.find("p", class_="location")
    print(title_el)
    print(company_el)
    print(loc_el)
    print()