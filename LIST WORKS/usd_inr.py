usd_inr_rates=[88.79,88.77,88.63,88.41,88.23,88.23]
total=0
for us in usd_inr_rates:
    total+=us
print(total)

avg = total//len(usd_inr_rates)
print(avg)



max_rate=max(usd_inr_rates)
print(max_rate)

min_rate=min(usd_inr_rates)
print(min_rate)

