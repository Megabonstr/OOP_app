"""                             Практика ООП.
        Реализуем программу с использованием классов, методов, экземпляров
        класса и различными атрибутами как самого класса так и его экземпляров      """

"""     Для примера создадим программу для пользователей приложения для саморазвития 
        В которой у каждого пользователя будет набор уникальных характеристик, которые
        будут развиваться со временем и при выполнении определенных условий. 
        Так же будет реализован учет количества пользователей и их наименований     """

"""     Для начала опишем структуру данных (характеристик) пользователя
        Создадим основной класс User                                                """


class User:
    users_id: int = 10000
    count_users: int = 0
    all_users: dict = {}

    # Конструктор для всех экземпляров класса (Объектов пользователя)
    def __init__(self, name: str, gender: str, age: int):
        """ При создании экземпляра класса инициализируем функцию для подсчета данных о пользователях """
        self.count_id_list()
        """ Обязательные атрибуты для каждого экземпляра класса (пользователя) """
        self.user_id: int = User.users_id  # В методе count_id_list() значение увеличивается на 1, делая id уникальным
        self.name = name
        self.gender = gender
        self.age = age
        """ Не обязательные атрибуты для ввода роста и веса пользователя, можно использовать для расчета 
            параметров "куклы" персонажа, а так же коэффициента соответствия роста и веса относительно нормы """
        self.height = None
        self.weight = None
        """ При создании экземпляра класса инициализируем функцию для хранения данных о пользователях """
        self.add_all_users()
        """ При создании экземпляра класса инициализируем функцию для определения базовых характеристик """
        self.user_params()

    @staticmethod
    def count_id_list():
        User.count_users += 1  # При создании экземпляра класса метод вызывается в __init__
        User.users_id += 1  # Так же вызывается в __init__ и текущее значение присваивается в self.user_id

    def add_all_users(self):
        User.all_users.update({self.users_id: self.name})  # Так же вызывается в __init__

    def user_params(self):
        self.strenght: int = 10  # Показатель физической силы, развивается при выполнении силовых упражнений
        self.endurance: int = 10  # Показатель выносливости, развивается при кардио тренировках - бег и тд.
        self.intellect: int = 10  # Показатель знаний, развивается при обучении, чтении книг, просмотра обучающих видео
        self.logic: int = 10  # Показатель сообразительности, развивается при решении сложных задач с помощью алгоритмов

    def get_user_info(self) -> str:
        return f' Характеристики {self.name} {self.gen} {self.age}:\n Сила: {self.strenght}\n Выносливость: {self.endurance}\n ' \
               f'Интеллект: {self.intellect}\n Мышление: {self.logic}'

    def char_phys_devel(self, strength_train, cardio_train) -> str:
        print(f'За каждый час тренировки, ваши характеристики увеличиваются на 0,1')
        self.strenght += strength_train / 10
        self.endurance += cardio_train / 10
        if strength_train > 0:
            return f'Ваша сила увеличена на {self.strenght}'
        if cardio_train > 0:
            return f'Ваша сила увеличена на {self.strenght}'

    def char_mind_devel(self, education, logic_ex):
        pass


user1 = User('Leon', 'муж.', 35)
user2 = User('Jane', 'жен.', 25)
user3 = User('Helicopter', 'вертолет', 15)

user3.char_phys_devel(
    int(input(f'Сколько вы занимались силовыми сегодня?:')),
    int(input(f'Сколько вы занимались кардио сегодня?:'))
)

print(user3.get_user_info())
print(User.all_users)
print(User.count_users)
print(user1.user_id)
print(user2.user_id)
print(user3.user_id)
