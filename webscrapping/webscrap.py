import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

job_cards = results.find_all("div", class_="card-content")

df = pd.DataFrame(columns=["Job", "Company", "Location"])

print(df)

for jc in job_cards:
    title_el = jc.find("h2", class_="title")
    company_el = jc.find("h3", class_="company")
    loc_el = jc.find("p", class_="location")
    df.loc[len(df)] = [title_el.text.strip(), company_el.text.strip(),
                       loc_el.text.strip()]

print(df.head())