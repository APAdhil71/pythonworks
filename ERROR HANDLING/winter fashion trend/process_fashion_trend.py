file_path="ERROR HANDLING\\winter fashion trend\\Winter_Fashion_Trends_Dataset.csv"
fr=open(file_path,"r",encoding="utf-8")
import csv
reader=csv.DictReader(fr)
data=[row for row in reader]
for row in data[:5]: #first five rows
    print(row)
print("Total rows:", len(data))
brands = {row["Brand"] for row in data}
print(brands)
category_count = {}
for row in data:
    cat = row["Category"]
    if cat in category_count:
        category_count[cat] += 1
    else:
        category_count[cat] = 1
print(category_count)
trending = [row for row in data if row["Trend_Status"] == "Trending"]
print(trending)   #show all trending products
outdated = sum(1 for row in data if row["Trend_Status"] == "Outdated")
print(outdated)
winter_2025 = [row for row in data if row["Season"] == "Winter 2025"]
print(winter_2025)
materials = {row["Material"] for row in data}
print(materials)
unisex_count = sum(1 for row in data if row["Gender"] == "Unisex")
print(unisex_count)
colors = set()
for row in data:
    colors.add(row["Color"])
for c in colors:
    # print(c)
    seasons= {row["Season"] for row in data}
print(seasons)


