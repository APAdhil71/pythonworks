file_path="C:\\Users\\adhil\\OneDrive\\Desktop\\pythonsworks\\ERROR HANDLING\\cart\\cart_items_100.csv"
fr=open(file_path,"r",encoding="utf-8")
import csv
reader=csv.DictReader(fr)
data=[row for row in reader]
order_summary={}
for o in data:
    title=o.get("title")
    qty=int(o.get("quantity"))
    if title in order_summary:
        order_summary[title]+=qty
    else:
        order_summary[title]=qty
print(order_summary)
max_val=max(order_summary.values())
popular_order=[k for k,v in order_summary.items() if v==max_val]
print(popular_order)
min_val=min(order_summary.values())
cheap_order=[k for k,v in order_summary.items() if v== min_val]
print(cheap_order)