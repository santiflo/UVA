from sys import stdin

def comparar(x,y):
    if x==y: return 0
    elif x>y: return 1
    else: return -1

def busqueda(n):
    ans = 1
    min = 1
    max = 10**100
    l = min
    r = max
    while True:
        m = (l+r)//2
        tm = m
        m*=m
        if m == n or ans == m:
            ans = m
            break
        elif comparar(m,n) == -1:
            ans = m
            l = tm
        else:
            r = tm
    return ans

def main():
    n = int(stdin.readline().strip())
    while n!= 0:
        print(busqueda(n))
        n = int(stdin.readline().strip())

main()