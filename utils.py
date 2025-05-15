import requests
from bs4 import BeautifulSoup
import csv

def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text

def parse_currency_table(html):
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table', class_='wikitable')

    target_table = None

    for table in tables:
        headers = [th.text.strip() for th in table.find_all('th')]
        if "Code" in headers and "Currency" in headers and ("Numeric" in headers or "Num" in headers):
            target_table = table
            break

    if not target_table:
        print("Не удалось найти нужную таблицу.")
        return

    rows = target_table.find_all('tr')[1:]
    data = []

    for row in rows:
        cols = row.find_all(['td', 'th'])
        if len(cols) >= 3:
            code = cols[0].text.strip()
            currency = cols[1].text.strip()
            num = cols[2].text.strip()
            data.append([code, currency, num])

    with open('currencies.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(['Code', 'Currency', 'Num'])
        writer.writerows(data)

    print("✅ Готово! Файл currencies.csv сохранён.")
