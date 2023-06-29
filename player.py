class Player:

    def __init__(self, name: str, age: int, nation: str, club: str):

        assert age >= 15, "Age must be greater than 15"

        self.__name = name
        self.__age = age
        self.__nation = nation
        self.__club = club

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

    @club.setter
    def club(self, new_club):
        self.__club = new_club

        
        