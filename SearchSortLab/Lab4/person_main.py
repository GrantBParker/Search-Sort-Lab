from comparable import Comparable
from personList import PersonList
from person import Person
from sort_search_funcs import *


def main():

    p_list = PersonList()
    p_list.populate("Persons.csv")

    print("List searched using linear search")
    print()
    
    name = input("Who do you want to search for?")
    bdate = input("What is their birthdate? (mm-dd-yyyy)")
    print()
    
    month, day, year = bdate.split('-')
    p_obj = Person(name,  int(month), int(day), int(year))

    index = p_list.search(linear_search, p_obj)

    if index == -1:
        print(name, "is not in the list")
    else:
        print(name, "is at position", index, "in the list")

    print()
    print("The number of compares are", Comparable.get_num_compares())
    print()
    
    Comparable.clear_compares()

    p_list.sort(bubble_sort)
    
    print("List sorted by bubble sort") 
    for p in p_list:
        print(p)

    print()
    print("The number of compares are", Comparable.get_num_compares())
    print()

    Comparable.clear_compares()

    print("List searched using binary search")
    print()
    
    name = input("Who do you want to search for?")
    bdate = input("What is their birthdate? (mm-dd-yyyy)")
    print()

    month, day, year = bdate.split('-')
    p_obj = Person(name, int (month), int(day), int(year))

    index = p_list.search(binary_search, p_obj)
    if index == -1:
        print(name, "is not in the list")
    else:
        print(name, "is at position", index, "in the list")

    print()
    print("The number of compares are", Comparable.get_num_compares())


main()
