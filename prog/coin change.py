def unique(coins, amount):
    coins.sort(reverse=True) 
    results = []
    dup = []
    for coin in coins:
        while amount >= coin:
            if coin not in dup:
                results.append(coin)
                amount -= coin
                dup.append(coin)
    if amount != 0:
        return "no combinations"  
    return results
coins = [1,1 ]
amount = 8
res = unique(coins, amount)
print("The combination is:", res)
