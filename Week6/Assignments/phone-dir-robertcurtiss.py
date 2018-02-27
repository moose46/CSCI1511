"""
Author: Robert W. Curtiss

Class: CSCI-1511
 -Project: CSCI1511
 -File: phone-dir-robertcurtiss.py
 -Created: Feb, 20th, 2018
Description:
creates and updates a phone directory
"""
import shelve as sh

the_phone_book_name = "thePhoneBook"


class Person():
    name = ""
    phone = ""
    new = False

    def __init__(self, name='XX', phone='YY'):
        self.name = name
        self.phone = phone

    def __str__(self):
        return "Name: " + self.name + " Phone: " + self.phone


def print_error():
    """prints an error message"""
    print("Incorrect Selection, try again!\n")


def show_menu():
    """displays an menu of functions for maintaining the database"""
    while True:
        try:
            display_menu()
            ans = int(input("Enter your selection [1-4]: "))
            if ans in range(1, 7):
                return ans
            raise ValueError()
        except Exception as Ex:
            print_error()
            continue


def display_menu():
    """display menu options"""
    print("""Menu Selection:
    1. Add Entry
    2. Update Entry
    3. Delete Entry
    4. Look Up Entry
    5. Show All Entries
    6. Exit\n""")


def create_default_data():
    """some data to play with during testing, stomps on database every time"""
    db = sh.open(the_phone_book_name, flag='n', writeback=True)
    phone_list = {'Bob': '6145617554',
                  'Leslie': '3095551212',
                  'Carol': '61455551212',
                  'Rick': '8955551212'}

    for name_key in phone_list:
        db[name_key] = phone_list[name_key]
    db.sync()
    db.close()


def get_new_entry(in_person):
    """collects and assigns data to a new person and return the person"""
    person = Person()
    person.name = get_name()
    person.phone = input("Enter Phone Number: ")
    return person


def delete_entry(key):
    """delete an entry from the database"""
    db = sh.open(the_phone_book_name, flag='c', writeback=True)
    if key in db:
        confirm = input("Delete {name} [y/n]: ".format(name=key))
        if confirm.lower() == 'y':
            print("Deleting entry ..... {name}\n".format(name=key))
            del db[key]


def db_add_entry(person):
    """either updates an existing entry or adds a new entry"""
    db = sh.open(the_phone_book_name, flag='c', writeback=True)
    if person.name in db:
        print("Updating existing entry ..... {name}\n".format(name=person.name))
    else:
        person.new = True
        print("Adding new entry ..... {name}".format(name=person.name))
    db[person.name.capitalize()] = person.phone
    db.sync()
    db.close()
    db_show_all()


def db_update_entry():
    """updates an existing entry"""
    db = sh.open(the_phone_book_name, flag='c', writeback=True)
    name = get_name()
    if name in db:
        phone_number = get_phone_number(db[name.capitalize()])
        print("Updating existing entry ..... {name}\n".format(name=name))
        db[name.capitalize()] = phone_number
        db.sync()
    else:
        print_error()
    db.close()
    db_show_all()


def find_entry(key):
    """Find a entry by phone number or name"""
    found_list = []
    db = sh.open(the_phone_book_name, flag='c', writeback=True)
    for k in db:
        name = str(k).lower()
        phone = str(db[k])
        if (name.find(key.lower())) >= 0 or (phone.find(key.lower()) >= 0):
            person = Person()
            person.name = k
            person.phone = db[k]
            found_list.append(person)
    display_list(found_list)
    db.close()


def display_list(the_list):
    """display a list of Persons if a list is provided"""
    print("\n===================================")
    for person in the_list:
        print("{name:12s}\t\t{phone}".format(name=person.name, phone=person.phone))
    if the_list == []:
        print("\nNo entries found!\n")
    print("===================================\n")


def db_show_all():
    """creates a list of all entry's in the database"""
    the_list = []
    db = sh.open(the_phone_book_name, flag='c', writeback=True)
    for key in db:
        person = Person()
        person.name = key
        person.phone = db[key]
        the_list.append(person)
    display_list(the_list)
    db.close()


def get_name():
    """get a person name and return it capitalized"""
    return input("Enter Name: ").capitalize()

def get_phone_number(phone_number):
    """get a person name and return it capitalized"""
    return input("Enter Updated Phone Number for {phone}: ".format(phone=phone_number))


def get_search_string():
    """get a string to search on"""
    return input("Enter search name, or phone number: ")


def main():
    """the main engine"""
    action = 12
    # create_default_data()
    while action > 0:
        action = show_menu()
        # Show all entries in the database
        # add new entry
        if action == 1:
            person = Person()
            person = get_new_entry(person)
            db_add_entry(person)
        elif action == 2:
            # update an entry

            db_update_entry()
        # delete an entry
        elif action == 3:
            delete_entry(get_name())
        elif action == 4:
            find_entry(get_search_string())
        elif action == 5:
            db_show_all()
        elif action == 6:
            break


print("\nPress enter to Exit")

main()
