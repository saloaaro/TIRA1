def count(t):
    price_counts = {}
    ways = 0

    for price in t:
        half_price = price / 2
        if half_price in price_counts:
            ways += price_counts[half_price]
        
        if price in price_counts:
            price_counts[price] += 1
        else:
            price_counts[price] = 1

    return ways

if __name__ == "__main__":
    print(count([1, 2, 3, 4]))  # 2
    print(count([1, 1, 1, 1]))  # 0
    print(count([1, 2, 1, 2, 1, 2]))  # 6
    print(count([5, 1, 3, 4, 1, 6]))  # 1


