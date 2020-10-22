# используется для сортировки
from operator import itemgetter

class House:
    """Дом"""
    def __init__(self, id, fio, sal, Street_id):
        self.id = id
        self.fio = fio
        self.sal = sal
        self.Street_id = Street_id

class Street:
    """Улица"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class HouseStreet:
    """
    'Дома на улице' для реализации
    связи многие-ко-многим
    """
    def __init__(self, Street_id, House_id):
        self.Street_id = Street_id
        self.House_id = House_id

# Улицы
Streets = [
    Street(1, 'Ярославское шоссе'),
    Street(2, 'Улица Чичерина'),
    Street(3, 'Улица Енисейская'),

]

# Дома
Houses = [
    House(1, '123', 25000, 1),
    House(2, '119к1', 35000, 2),
    House(3, '34', 45000, 3),
    House(4, '36А', 35000, 3),
    House(5, '8к2', 25000, 3),
]

Houses_Streets = [
    HouseStreet(1,1),
    HouseStreet(2,2),
    HouseStreet(3,3),
    HouseStreet(3,4),
    HouseStreet(3,5),

]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим 
    one_to_many = [(e.fio, e.sal, d.name) 
        for d in Streets 
        for e in Houses 
        if e.Street_id==d.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_tHouse = [(d.name, ed.Street_id, ed.House_id) 
        for d in Streets 
        for ed in Houses_Streets 
        if d.id==ed.Street_id]
    
    many_to_many = [(e.fio, e.sal, Street_name) 
        for Street_name, Street_id, House_id in many_to_many_tHouse
        for e in Houses if e.id==House_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)
    
    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все отделы
    for d in Streets:
        # Список домов
        d_Houses = list(filter(lambda i: i[2]==d.name, one_to_many))
        # Если улица не пустой
        if len(d_Houses) > 0:
            # Цены на дома
            d_sals = [sal for _,sal,_ in d_Houses]
            # Суммарная стоимость домов
            d_sals_sum = sum(d_sals)
            res_12_unsorted.append((d.name, d_sals_sum))

    # Сортировка по суммарной стоимости домов
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    # Перебираем улицы
    for d in Streets:
        if 'Чичерина' in d.name:
            # Список улиц
            d_Houses = list(filter(lambda i: i[2]==d.name, many_to_many))
            # Только дома
            d_Houses_names = [x for x,_,_ in d_Houses]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список домов
            res_13[d.name] = d_Houses_names

    print(res_13)

if __name__ == '__main__':
    main()

