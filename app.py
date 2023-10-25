from bs4 import BeautifulSoup
import requests

url = 'http://www.scrapethissite.com/pages/forms/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')
#print(soup.prettify())

#extracted_data = soup.find('p', class_='lead').text
#print(extracted_data)

print(soup.find('th').text)
for td in soup.findAll('td',class_='name'):
    print(td.text)