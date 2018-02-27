import shelve as sh

the_phone_book_name = "thePhoneBook"


class Person():
    name = ""
    phone = ""

    def __init__(self, name='XX', phone='YY'):
        self.name = name
        self.phone = phone

    def __str__(self):
        return "Name: " + self.name + " Phone: " + self.phone


def print_error():
    print("Incorrect Selection, try again!\n")


def show_menu():
    while True:
        try:
            display_menu()
            ans = int(input("Enter your selection [1-4]: "))
            if ans >= 1 and ans <= 5:
                return ans
            raise ValueError()
        except Exception as Ex:
            print_error()
            continue


def display_menu():
    print("""Menu Selection:
    1. Add Entry
    2. Delete Entry
    3. Look Up Entry
    4. Show All Entries
    5. Exit\n""")


def create_default_data():
    db = sh.open(the_phone_book_name, flag='n', writeback=True)
    phone_list = {'Bob': '6145617554',
                  'Leslie': '3095551212',
                  'Carol': '61455551212',
                  'Rick': '8955551212'}

    for k in phone_list:
        db[k] = phone_list[k]
    db.sync()
    db.close()


def get_new_entry():
    person = Person()
    person.name = get_name()
    person.phone = input("Enter Phone Number: ")
    return person


def delete_entry(key):
    db = sh.open(the_phone_book_name, flag='c', writeback=True)
    if key in db:
        confirm = input("Delete {name} [y/n]: ".format(name=key))
        if confirm.lower() == 'y':
            print("Deleting entry ..... {name}\n".format(name=key))
            del db[key]


def db_add_entry(person):
    db = sh.open(the_phone_book_name, flag='c', writeback=True)
    if person.name in db:
        print("Updating entry ..... {name}\n".format(name=person.name))


    db[person.name.capitalize()] = person.phone
    db.sync()
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
    print("\n===================================")
    for person in the_list:
        print("{name:12s}\t\t{phone}".format(name=person.name, phone=person.phone))
    if the_list == []:
        print("\nNo entries found!\n")
    print("===================================\n")


def db_show_all():
    the_list = []
    db = sh.open(the_phone_book_name, flag='c', writeback=True)
    for key in db:
        person = Person()
        person.name = key
        person.phone = db[key]
        the_list.append(person)

    display_list(the_list)
    # print("{name:12s}\t\t{phone}".format(name=key, phone=db[key]))

    db.close()


def get_name():
    return input("Enter Name: ").capitalize()


def get_search_string():
    return input("Enter search name, or phone number: ")


def main():
    action = 12
    # create_default_data()
    while action > 0:
        action = show_menu()
        # Show all entries in the database
        # add new entry
        if action == 1:
            person = get_new_entry()
            db_add_entry(person)
        # delete an entry
        elif action == 2:
            delete_entry(get_name())
        elif action == 3:
            find_entry(get_search_string())
        elif action == 4:
            db_show_all()
        elif action == 5:
            break


print("\nPress enter to Exit")

main()
