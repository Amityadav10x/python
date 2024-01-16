number = 5

if(number%2==0):
    print("number is even")
else:
    print("number is odd")


cost_price = 100
selling_price = 150

if(selling_price>cost_price):
    profit = selling_price-cost_price
    print("seller has profit")
elif(selling_price==cost_price):
    print("no profit no lose")
else:
    loss = cost_price < selling_price
    print("seller occured loss",)
