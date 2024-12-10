# импортирую библиотеку для того чтобы генерировать случайноые числа
import numpy as np


# Создаю функцию, которая будет находить загаданное число меньше чем за 20 попыток
def game_core_v3(number: int = 1) -> int:
    """ Функция ищет случайное число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # тут будет храниться количество итераций,
    # которое соответствует количеству попыток для нахождения случайно сгенерированного числа
    count = 0
    # загаданное число помещаем в переменную для удобства
    predict = np.random.randint(1, 101)
    # сравниваем числа, чтобы менять значение переменной predict
    while number != predict:
        # количество попыток нахождения
        count += 1
        # прописываю условия на случай того если программа сгенерировала число меньше загаданного
        if number > predict:
            # разница между загаданным и сгенерированным число нужна для дальнеших условий
            difference = number - predict
            # на случай если разница отрицательная
            if difference < 0:
                difference *= -1
            # если разница меньше 10, то увеличиваю сгенерированное число на 1
            if difference < 10:
                predict += 1
            # добавлем болшее число чтобы соответствовать условию -
            # количество попыток меньше 20    
            if difference >= 10 and difference < 40:
                predict += 5     
            # то же самое, но уже 15    
            if difference >= 40 and difference <= 100:
                predict += 15    
        # на случай если загаданное число меньше сгенерированного
        if number < predict:
            # соответствуем условию - количество попыток нахождени числа програмой меньше 20 
            difference_v2 = predict - number
            if difference_v2 < 0:
                difference_v2 *= -1
            if difference_v2 < 10:
                predict -= 1     
            if difference_v2 >= 10 and difference_v2 < 40:
                predict -= 5
            if difference_v2 >= 40 and difference_v2 <= 100:
                predict -= 15     
                                                
    return count

def score_game(game_core_v3) -> int:
    """за какое количество попыток в среденем за 10000 подходов угадывает наш алгорит

    Args:
        game_core_v3 (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # можно посмотреть одну и ту же генерацию случайных чисел
    np.random.seed(1)
    # пополняе список чисел случайно сгенерированными числами
    random_array = np.random.randint(1, 100, size=(10000))  
    # пополняем количеством угадываний для нахождения среднего значения
    for number in random_array:
        count_ls.append(game_core_v3(number))
    # узнаем среднее значение
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
               
# смотрим на результат
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
               
    