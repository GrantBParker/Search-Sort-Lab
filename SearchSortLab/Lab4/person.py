from comparable import Comparable
from date import Date


class Person(Comparable):

    def __init__(self, name, month, day, year ):

        self.__name = name
        self.__birthday = Date(month, day, year)

    def get_name(self):

                return self.__name

    def get_birthday(self):

                return self.__birthday

    def compare(self, other_Person):

        Comparable.compare(other_Person)

        if self.__birthday.compare(other_Person.get_birthday()) > 0:

            return 1

        elif self.__birthday.compare(other_Person.get_birthday()) < 0:

            return -1

        elif self.__name > other_Person.get_name():

            return 1

        elif self.__name < other_Person.get_name():

            return -1

        else:

            return 0

    def __str__(self):

        return str(self.__name) + "-" + str(self.__birthday)
