import requests
from bs4 import BeautifulSoup
url = "https://contentitvedant.github.io/Railway_Booking/index.html"
response = requests.get(url)
print("Status Code:", response.status_code)
print("Page Fetched Successfully")

print()

import requests
from bs4 import BeautifulSoup
url = "https://contentitvedant.github.io/Railway_Booking/trains.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
train_numbers = soup.find_all(class_="train-number")
print("Train Numbers on IndRail:")
print("=" * 30)
for item in train_numbers:
    print(item.get_text())

print()

import requests
from bs4 import BeautifulSoup
url = "https://contentitvedant.github.io/Railway_Booking/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("tbody").find_all("tr")
print("Train Schedule:")
print("=" * 60)

for row in rows:
    cells = row.find_all("td")
    train_no = cells[0].get_text()
    train_name = cells[1].get_text()
    from_stn = cells[2].get_text()
    to_stn = cells[3].get_text()
    departure = cells[4].get_text()
    arrival = cells[5].get_text()
    duration = cells[6].get_text()

    
    print(train_no, "|", train_name)
    print("   From :", from_stn, "-> To :", to_stn)
    print("   Departure :", departure, "| Arrival :", arrival, "| Duration :", duration)
    print("-" * 60)
