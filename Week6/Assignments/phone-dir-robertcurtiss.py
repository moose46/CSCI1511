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


db = sh.open(the_phone_book_name, flag='n', writeback=True)
phone_list = {'Bob': '6145617554',
              'Leslie': '3095551212',
              'Carol': '61455551212',
              'Rick': '8955551212'}

for k in phone_list:
    db[k] = phone_list[k]
name = Person()
name.name = "Bobby"
name.phone = "6145551212"

db["persons"] = name

db.sync()
db.close()
db = sh.open(the_phone_book_name, flag='c', writeback=True)
for key in db:
    if (key == 'persons'):
        person = db[key]
        print(person)
    else:
        print(key, db[key])

if 'Bob' in db:
    print('Hello - ', db['Leslie'])
db.close()
