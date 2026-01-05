product={"code":"2000",
         "title":"bmw",
         "category":"car",
         "price":"2cr",
         "avl_qty":"2"}

print(product["title"])
if "price" in product:
    print(product["price"])
else:
    print("key not exist")

    #add avl qty
if "avl_qty" in product:
    product["avl_qty"]=+10
else:
    product["avl_qty"]=15
print(product)
