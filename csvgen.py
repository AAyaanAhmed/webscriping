import requests
import csv
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

try:
    res = requests.get(url, timeout=5)

    if res.ok:
        soup = BeautifulSoup(res.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        with open("books.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["Title", "Price", "Availability"])

            for b in books:
                title = b.h3.a["title"]
                price = b.find("p", class_="price_color").text
                stock = b.find("p", class_="instock availability").text.strip()

                w.writerow([title, price, stock])

        print("Data saved to books.csv")

    else:
        print("Failed:", res.status_code)

except requests.ConnectionError:
    print("Connection error.")

except requests.Timeout:
    print("Request timed out.")

except Exception as e:
    print("Error:", e)
