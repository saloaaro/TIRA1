def create(n):
    if n < 1:
        return []

    lista = [n]  

    while n > 1:
        
        next_num = lista[-1] - n
        if next_num <= 0 or next_num in lista:
            next_num = lista[-1] + n
        lista.append(next_num)
        n -= 1

    return lista[::-1]

if __name__ == "__main__":
    print(create(6))  # [3, 1, 6, 2, 4, 5]
    print(create(10))  # [7, 10, 3, 1, 5, 4, 8, 6, 9, 2]
    print(create(15))  # [9, 4, 6, 14, 15, 13, 12, 11, 5, 2, 3, 8, 1, 7, 10]
