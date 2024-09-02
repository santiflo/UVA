from sys import stdin

def operation_0(l, p , q):
    p, q = p-1, q-1
    if l[p] != l[q]:
        l[p] = l[p] | l[q]
        l[q] = l[p]
    return l

def operation_1(l, p , q):
    if l[p-1] != l[q-1]:
        a = list(l[p-1]) + list(l[q-1])
        for i in a: 
            l[i-1] = set(a)
    return l

def operation_2(l, p, q):
    if l[p-1] != l[q-1]:
        a = list(l[p-1])
        a.remove(p)
        for i in a:
            l[i-1] = set(a)
        l[p-1] = {p} | l[q-1]
        l[q-1] = l[p-1]
    return l

def operation_3(l, p):
    print(len(l[p-1]), sum(l[p-1]))

def main():
    line = stdin.readline().strip()
    while line != '':
        max, instructions = list(map(int,line.split()))
        l = [{i} for i in range(1,int(max)+1)]
        while instructions > 0:
            instruction = list(map(int,stdin.readline().strip().split()))
            if instruction[0]==1: 
                operation_1(l, instruction[1], instruction[2])
            elif instruction[0]==2: 
                operation_2(l, instruction[1], instruction[2])
            elif instruction[0]==3:
                operation_3(l, instruction[1])
            else: print('La operacion no existe')
            instructions -= 1
        line = stdin.readline().strip()
main()