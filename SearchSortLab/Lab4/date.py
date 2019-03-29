from comparable import Comparable


class Date(Comparable):

    def __init__(self, month, day, year):

        self.__day = day
        self.__year = year
        self.__month = month


    def get_day(self):

        return self.__day

    def get_month(self):

                return self.__month

    def get_year(self):

                    return self.__year

    def compare(self, other_Date):

                if  self.__year > other_Date.get_year():

                    return 1


                elif self.__year < other_Date.get_year():

                    return -1

                elif self.__month > other_Date.get_month():

                    return 1


                elif self.__month < other_Date.get_month():

                    return -1

                elif self.__day > other_Date.get_day():

                    return 1

                elif self.__day < other_Date.get_day():

                    return -1

                else:
                    return 0

    def __str__(self):

        return str(self.__month) + "-" + str(self.__day) + "-" + str(self.__year)
