trains = [
    {"train_no": "101", "train_name": "Konkan Express"},
    {"train_no": "102", "train_name": "Rajdhani Express"},
    {"train_no": "103", "train_name": "Vande Bharat"},
    {"train_no": "104", "train_name": "Deccan Express"}
]

# Step 1: Store train schedule
file = open("train_schedule.txt", "w")

for t in scraper.get_train_schedule():
    file.write(
        t["train_no"] + " - " +
        t["train_name"] + "\n"
    )

file.close()

print("Train schedule saved successfully.")

