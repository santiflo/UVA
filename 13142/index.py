from sys import stdin

def calcular_masa(t, d):
    d = d * 1000 * 1000
    t = t * 60 * 60 * 24
    m = int(d/t)
    if m > 0:
        print('Remove '+ str(m) +' tons')
    else:
        print('Add '+ str(abs(m)) +' tons')

def main():
    casos = int(stdin.readline().strip())
    while casos > 0:
        t, s, d = list(map(int,stdin.readline().strip().split()))
        calcular_masa(t, d)
        casos -= 1

main()