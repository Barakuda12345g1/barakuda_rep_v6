"""Игра угадай чисо.
Компютер сам угадывает число
    """

import numpy as np

def random_predict(number:int=1) -> int:
    """Унадываем число случайным образом

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """    
    # обьявлем переменную в глобальной области видимости,
    # чтобы в дальнейше изменять через функцию
    count = 0    
    # через луп будем считать колтчество попыток
    while True:
        # считаем количестово итераций
        count += 1
        # выбираемое случайным образом число записываем
        # в переменную, чтобы использовать в дальнейшем
        # для сравнения
        predict_number = np.random.randint(1, 101)
        # если числа совпадают то завершаем луп
        if number == predict_number:
            break
    return count
    # не ввожу в функцию аргумент,
    # потому что он задан как именнованый

        
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем
    из 1000 подходов угадывает наш алгоритом

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """            
    # список для хранения количества попыток
    count_ls = []
    # фиксируем сид для воспроизводимости
    np.random.seed(1)
    # загадали список из тысячи чисел, которые
    # последовательно будут вводиться в 
    # функцию random_predict
    random_array = np.random.randint(1, 101, size=(1000))
    # находим количество попыток нахождения 
    # загаданного числа, которых тысяча
    for number in random_array:
        # пополняем список количеством попыток для каждого
        # загаданного числа
        count_ls.append(random_predict(number))
    # находим среднее, сумма количества попыток деленная 
    # на тысячу 
    score = int(np.mean(count_ls))
    # красиво печатаем код
    print(f'Ваш алгоритм угадывает число в среднем за:\
        за {score} попыток')
    return score

# исполняемый файл импортируем корректно
if __name__ == '__main__':
    score_game(random_predict)