file_path="Errorhandling\\instagram\\Instagram_Analytics.csv"
fr=open(file_path,"r",encoding="utf-8")
import csv
reader=csv.DictReader(fr)
data =[row for row in reader]
high_likes = [row["post_id"] for row in data if float(row["likes"]) > 100000]
# print(high_likes)
# print("Total posts with likes = 100000 =", len(high_likes))
media_count = {}
for row in data:
    m = row["media_type"]
    if m in media_count:
        media_count[m] += 1
    else:
        media_count[m] = 1
# print(media_count)
high_comments = [row["post_id"] for row in data if float(row["comments"]) > 9000]
# print(high_comments)
# print("high comment above 9000 :",len(high_comments))
# print("Total data =", len(data))
avg_likes = sum(float(row["likes"]) for row in data) / len(data)
# print(avg_likes)
avg_comment = sum(float(row["comments"]) for row in data) / len(data)
# print(avg_comment)
category_count = {}
for row in data:
    cat = row["content_category"]
    if cat in category_count:
        category_count[cat] += 1
    else:
        category_count[cat] = 1
# print(category_count)
traffic_count = {}
for row in data:
    t = row["traffic_source"]
    if t in traffic_count:
        traffic_count[t] += 1
    else:
        traffic_count[t] = 1
# print(traffic_count)
reels = sum(1 for row in data if row["media_type"] == "Reel")
photos = sum(1 for row in data if row["media_type"] == "Photo")
videos = sum(1 for row in data if row["media_type"] == "Video")
print("Reels:", reels)
print("Photos:", photos)
print("Videos:", videos)

