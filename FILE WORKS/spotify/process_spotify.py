file_path="file_works\\spotify\\spotify_data clean.csv"
import csv
fr=open(file_path,"r",encoding="utf-8-sig")
reader =csv.DictReader(fr)

data = [row for row in reader]
first_five_tracks=[p.get("track_name")for p in data[:5]]
print(first_five_tracks)
print("total rows=",len(data))

all_artist=[p.get("artist_name") for p in data]
unique_artist_set=set(all_artist)
# print(unique_artist_set)

popular_track=[p.get("track_name") for p in data if int(p.get("track_popularity"))>50]
# print(popular_track)

