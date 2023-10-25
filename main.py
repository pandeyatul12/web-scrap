from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.findAll('table')[1]
#print(soup)
world_titles = table.findAll('th')
world_table_titles = [titles.text.strip() for titles in world_titles]
#print(world_table_titles)

df = pd.DataFrame(columns = world_table_titles)
#print(df)

column_data = table.findAll('tr')
#print(column_data)

for row in column_data[1:]:
    row_data = row.findAll('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data

df.to_csv(r"D:\Mine\GitHub\web-scrap\Top Companies.csv", index=False)
