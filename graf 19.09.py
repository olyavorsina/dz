import math
def task1(n, m,):
    k = 1
    V = n * m * k 
    #Находим объем памяти этого изображения
    return int (V)

def task2(before, after,):
    result = after / before 
    #Находим во сколько раз увеличился объем памяти
    return int (result)

def task3(nn, mm, vv):
    vv = vv * 1024 * 8 
    #Нереводим Кб в биты
    k = vv / (nn * mm) 
    #Определяем количество цветов
    return int (k)

def task4 (k, vvv):
    vvv = vvv * 8 
    #Переводим из байты в бит
    k = math.log2 (k) 
    #Узнаем сколько бит в одной точке
    mn = vvv / k 
    #Количество точек на экране
    return int (mn)
    




if __name__ == "__main__" :
    #n = int (input("Ширина: "))
    #m = int (input("Высота: "))
    #print (task1(n, m))
    #before = int (input("Количество цветов до: "))
    #after = int (input("Количество цветов после: "))
    #print (task2(before, after))
    #nn = int (input("Ширина: "))
    #mm = int (input("Высота: "))
    #vv = int (input("Объем памяти: "))
    #print (task3(nn, mm, vv))
    k = int (input("Количество цветов: "))
    vvv = int (input("Объем памяти: "))
    print (task4(k, vvv))