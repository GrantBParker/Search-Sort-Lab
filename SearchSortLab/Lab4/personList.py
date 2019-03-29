import csv
from person import Person
from  sortable import Sortable
from searchable import Searchable


class PersonList(list, Sortable, Searchable):

    def __init__(self):

        super().__init__()

    def person__at(self, index):

        return self[index]

    def populate(self, filename):

        try:
            with open(filename, 'r') as input_file:
                lines = csv.reader(input_file)
                person_list = list(lines)
            for person in person_list:
                name = person[0].strip()
                month = int(person[1].strip())
                day = int(person[2].strip())
                year = int(person[3].strip())
                person1 = Person(name, month, day, year)
                self.append(person1)

        except IOError:
            print("File Open Error.")

    def sort(self, func):

        return func(self)

    def search(self, func, person):
        return func(self, person)

    def __str__(self):

        a = " "

        for person in self:

            a = str(person)

        return (a)
