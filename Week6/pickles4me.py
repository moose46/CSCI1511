import pickle, shelve as sh

theCode = """v = ["dill","sweet","hot"]

f = open("pickles.dat","wb")
pickle.dump(v,f)
f.close()

f = open("pickles.dat","rb")

variety = pickle.load(f)
print("======= pickle ============")
print(variety)
f.close()

lang = {'languages': ["c#","python","jquery","sql"]}
dogs = {'dogs' : ["lab","boxer","cocker spaniel","pit bull"]}
db = sh.open("lang.dat","n")
db['bob'] = lang
db['dog'] = dogs
db.sync()
db.close()
print("====== shelf ===========")
db = sh.open("lang.dat","r")
for key in db:
    print(db[key])
db.close()"""

v = ["dill","sweet","hot"]

f = open("pickles.dat","wb")
pickle.dump(v,f)
f.close()

f = open("pickles.dat","rb")

variety = pickle.load(f)
print("======= pickle ============\n")
print(variety)
f.close()

lang = {'languages': ["c#","python","jquery","sql"]}
dogs = {'dogs' : ["lab","boxer","cocker spaniel","pit bull"]}
db = sh.open("lang.dat","n")
db['lang'] = lang
db['dog'] = dogs
db.sync()
db.close()
print("\n====== shelf ===========\n")
db = sh.open("lang.dat","r")
for key in db:
    print(db[key])
db.close()
print("\n====== the code ===========\n")

# print(theCode)