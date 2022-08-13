from cmath import inf


prices = [7, 1, 5, 3, 6, 4]
#Output: 5
profit=0
min_buy=float(inf)
for price in prices:
    min_buy=min(min_buy,price)
    profit=max(profit,price-min_buy)
print(profit)
    

