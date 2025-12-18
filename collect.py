from bs4 import BeautifulSoup
import os
import pandas as pd

data = {'title': [], 'price': [], 'rating': [], 'description': [], 'discount': []}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}", "r", encoding="utf-8") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, "html.parser")

        t = soup.find("div", attrs={"class": "KzDlHZ"})
        title = t.get_text().strip() if t else "N/A"

        p = soup.find("div", attrs={"class": "Nx9bqj _4b5DiR"})
        price = p.get_text().strip() if p else "N/A"

        r = soup.find("span", attrs={"class": "Wphh3N"})
        rating = r.get_text().strip() if r else "N/A"

        desc = soup.find("div", attrs={"class": "_6NESgJ"})
        description = desc.get_text().strip() if desc else "N/A"

        di = soup.find("div", attrs={"class": "UkUFwK"})
        discount = di.get_text().strip() if di else "N/A"

        data['title'].append(title)
        data['price'].append(price)
        data['rating'].append(rating)
        data['description'].append(description)
        data['discount'].append(discount)

    except Exception as e:
        print(f"Error processing file {file}: {e}")

df = pd.DataFrame(data)

df.to_csv("smartwatchcsv", index=False)

print("Data extraction complete.")
