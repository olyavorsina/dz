import math
#def tasks1(a, b, c, d):
    #N = 2 ** (a / (b * c * d))
    #return int(N)

#if __name__ == "__main__":
    #inp1 = int(input("Введите количество бит: "))
    #inp2 = int(input("Введите количество страниц: "))
    #inp3 = int(input("Введите количество строк: "))
    #inp4 = int(input("Введите количество символов: "))
    #print(tasks1(inp1, inp2, inp3, inp4))

#def tasks2(a, b):
        #i = (math.log2(a))  / (math.log2(b))
        #return float(i)

#if __name__ == "__main__":
    #inp1 = float(input("Введите данные первого текста: "))
    #inp2 = float(input("Введите данные второго текста: "))
    #print(tasks2(inp1, inp2))

def tasks3(b, c):
    i = b / (math.log2(c))
    return int (i)

if __name__ == "__main__":
    inp1 = int (input("Введите количество бит: "))
    inp2 = int (input("Введите количество символов: "))
    print(tasks3(inp1, inp2))


