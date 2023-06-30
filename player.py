class Player:

    RATE = 0.7

    def __init__(
        self, name: str, age: int, nation: str, club: str,
        salary: float, position: str
    ):

        assert age >= 15, "Age must be greater than 15"

        self.__name = name
        self.__age = age
        self.__nation = nation
        self.__club = club
        self.__salary = salary
        self.__position = position

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def nation(self):
        return self.__nation

    @property
    def club(self):
        return self.__club

    @property
    def salary(self):
        return self.__salary

    @property
    def position(self):
        return self.__position

    @club.setter
    def club(self, new_club):
        self.__club = new_club

    @salary.setter
    def salary(self, new_salary):
        self.__salary = new_salary

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    @staticmethod
    def is_player_rich(salary):
        return salary > 100000