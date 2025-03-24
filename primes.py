def count(n):
    total = []
    for numero in range(2, n+1):
        for i in range(2, numero):
            if (numero % i) == 0:
                break
        else:
            total.append(numero)

    return len(total)       

    
if __name__ == "__main__":
    print(count(2)) # 1
    print(count(10)) # 4
    print(count(11)) # 5
    print(count(100)) # 25
    print(count(1000)) # 168