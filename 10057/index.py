from sys import stdin


def main():
    n = stdin.readline().strip()
    while n != '':
        numeros = []
        for _ in range(int(n)):
            numeros.append(int(stdin.readline().strip()))
        n = len(numeros)
        numeros.sort()
        es_impar = n%2 != 0
        min_mediana, max_mediana = 0, 0
        # Encontrar el minimo valor para A
        if es_impar:
            min_mediana = numeros[n//2]
            max_mediana = numeros[n//2]
        else:
            min_mediana = numeros[(n//2)-1]
            max_mediana = numeros[(n//2)]

        # Encontrar la cantidad de numeros igual a la mediana
        cantidad = 0
        for i in numeros:
            if i==min_mediana or i==max_mediana:
                cantidad += 1

        posibles_mediana = 0
        if es_impar:
            posibles_mediana = 1
        else:
            posibles_mediana = max_mediana - min_mediana + 1
        print(min_mediana, cantidad, posibles_mediana)
        n = stdin.readline().strip()
main()