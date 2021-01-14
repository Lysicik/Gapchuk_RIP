# поведенческий паттерн проектирования
# наблюдатель
# предметная область: магазин одежды делает рассылку подписчикам, при поступлении нового товара


from abc import ABC, abstractmethod



# абстрактный класс издателя
class Publisher(ABC):

    @abstractmethod
    def attach(self, subscriber):
        pass

    @abstractmethod
    def detach(self, subscriber):
        pass

    @abstractmethod
    def notify(self):
        pass


# абстрактный класс подписчика(наблюдателя)
class Subscriber(ABC):

    @abstractmethod
    def update(self, publisher):
        pass


# магазин, оповещающий подписчиков
class StorePublisher(Publisher):

    def __init__(self):
        self.new_goods = ''
        self.subscribers = []

    def attach(self, subscriber):
        self.subscribers.append(subscriber)
        return "Publisher:" + f"Добавлен новый подписчик с ником {subscriber.name}"

    def detach(self, subscriber):
        self.subscribers.remove(subscriber)
        return "Publisher:" + f"Удален подписчик с ником {subscriber.name}"

    def notify(self):
        print("Publisher:" + "Оповещаю подписчиков...")
        subscribers_reacts = []
        for subscriber in self.subscribers:
            subscribers_reacts.append(subscriber.update(self))
        for react in subscribers_reacts:
            if react != 1:
                print(react)

    def goods_arrival(self, goods):
        self.new_goods = goods
        print("Publisher:" + f"Поступил новый товар - {self.new_goods}")
        self.notify()


# Человек, подписавшиея на оповещения о поступлении кроссовок
class SneakersSubscriber(Subscriber):

    def __init__(self, name):
        self.name = name

    def update(self, publisher):
        if publisher.new_goods == "кроссовки":
            react = "SneakersSubscriber:" + f"{self.name} реагирует на новое поступление кроссовок"
            return react
        else:
            return 1


# Человек, подписавшиеся на оповещения о поступлении толстовки
class HoodiesSubscriber(Subscriber):

    def __init__(self, name):
        self.name = name

    def update(self, publisher):
        if publisher.new_goods == "толстовка":
            react = "HoodiesSubscriber:" + f"{self.name} реагирует на новое поступление толстовки"
            return react
        else:
            return 1


def client_code():
    store = StorePublisher()

    first_sneakers_subscriber = SneakersSubscriber("Серега")
    print(store.attach(first_sneakers_subscriber))
    second_sneakers_subscriber = SneakersSubscriber("Сашка")
    print(store.attach(second_sneakers_subscriber))
    first_hoodies_subscriber = HoodiesSubscriber("Вика")
    print(store.attach(first_hoodies_subscriber))

    print('\n')

    store.goods_arrival("кроссовки")
    store.goods_arrival("толстовка")

    print('\n')

    print(store.detach(first_sneakers_subscriber))

    print('\n')

    store.goods_arrival("кроссовки")


if __name__ == "__main__":
    client_code()