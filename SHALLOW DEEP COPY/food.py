from copy import copy
from copy import deepcopy
arun_fav_food=[
    ["dosa","tea"],
    ["meals","lime juice"],
    ["chapathi","lime tea"]
]
resin_fav_food=deepcopy(arun_fav_food)
resin_fav_food[0][0]="idili"
print("arun",arun_fav_food)
print("resin",resin_fav_food)