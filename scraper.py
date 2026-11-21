import requests
from bs4 import BeautifulSoup
import csv

with open("book.csv", "w", newline="", encoding="utf-8-sig") as f:
  writer = csv.writer(f)
  writer.writerow(["Title", "Price"])
  for n in range(1, 51):
      url = f"https://books.toscrape.com/catalogue/page-{n}.html"
      response = requests.get(url)
      response.encoding = "utf-8"
      soup = BeautifulSoup(response.text, "html.parser")
      books = soup.find_all("article", class_="product_pod")
      for book in books:
          title = book.find("h3").find("a")["title"]
          price = book.find("p", class_="price_color").text
          writer.writerow([title, price])


print(len(books))