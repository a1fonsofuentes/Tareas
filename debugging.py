def divisores(num):
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores        

def run():
    num = int(input("Ingresa un número: "))
    print(divisores(num))
    print("Finalizó el programa")

if __name__ == "__main__":
    run()


