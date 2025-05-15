from utils import fetch_page, parse_currency_table

def main():
    url = "https://en.wikipedia.org/wiki/ISO_4217"
    html = fetch_page(url)
    parse_currency_table(html)

if __name__ == "__main__":
    main()
