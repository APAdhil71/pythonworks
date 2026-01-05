menu_items={"poratta":9,
            "beef curry":60,
            "lime juice":20,
            "meals":130,
            "briyani":150,
            "fruit salad":200
}
for k in menu_items.keys():
    print(k)
for k,v in menu_items.items():
    print(k,v)
#display all menu_items names available under 50
for k,v in menu_items.items():
    if v>9:
        print(k,v)
item=menu_items.get("fruitsalad",0)
print(item)
if "lime juice" in  menu_items:
    menu_items["lime juice"]+=15
print(menu_items)