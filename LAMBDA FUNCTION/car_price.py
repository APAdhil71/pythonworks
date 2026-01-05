cars_price={
    "bmw" : 2300000,
    "benz": 1120000,
    "belono": 900000,
    "swift" : 750000
}
srt_car=sorted(cars_price,key=lambda k:cars_price.get(k),reverse=True)
print(srt_car)