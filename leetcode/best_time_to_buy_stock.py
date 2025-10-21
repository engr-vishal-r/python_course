def best_time_to_buy_sell(prices):
    min_price = float('inf')
    max_profit = 0
    buy_day = sell_day = 0
    temp_day = 0
    
    for i, price in enumerate(prices):
        if price < min_price:
            min_price = price
            temp_day = i 
        elif price - min_price > max_profit:
            max_profit = price - min_price
            buy_day = temp_day
            sell_day = i
    
    return max_profit, buy_day+1, sell_day+1

prices = [7, 1, 5, 3, 6, 4]
profit, buy, sell = best_time_to_buy_sell(prices)
print(f"Buy on day {buy}, Sell on day {sell}, Max Profit: {profit}")