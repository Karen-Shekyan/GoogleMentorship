import sqlite3

db = sqlite3.connect("user.db", check_same_thread=False) #CRUCIAL
global c
c = db.cursor()

# making tables
c.execute("CREATE TABLE if not exists users(username TEXT, password TEXT, email TEXT)")

# general method that can be used to get data easier
def select_from(database, table, data_want, datagive, datatype_give):
    db = sqlite3.connect(database, check_same_thread=False)
    c = db.cursor()
    temp = ((c.execute(f"SELECT {data_want} FROM {table} WHERE {datatype_give} = '{datagive}'")).fetchall())
    if(len(temp) > 0):
        return temp[0][0]
    else:
        return 0

def username_in_system(username):
    db = sqlite3.connect("user.db", check_same_thread=False)
    c = db.cursor()
    temp = list(c.execute("SELECT username FROM users").fetchall())
    for element in temp:
        for element2 in element:
            if username == element2:
                return True
    return False

def signup(username, password, email):
    db = sqlite3.connect("user.db", check_same_thread=False)
    c = db.cursor()
    if(username_in_system(username)):
        return False
    else:
        c.execute("INSERT INTO users VALUES (?,?,?)", (username, password, email))
    db.commit()
    return True #save changes

def remove_user(username):
    db = sqlite3.connect("user.db", check_same_thread=False)
    c = db.cursor()
    try:
        c.execute(f'DELETE FROM users WHERE username = "{username}"')
        db.commit()
        return True
    except:
        return False

# to verify if the password given is right to login
def login(username, password):
    db = sqlite3.connect("user.db", check_same_thread=False)
    c = db.cursor()
    if(username_in_system(username)):
        if(select_from("user.db", "users", "password", username, "username") == password):
            return True
    return False

def get_email(username):
    db = sqlite3.connect("user.db", check_same_thread=False)
    c = db.cursor()
    if (select_from("user.db", "users", "username", username, "username") != 0):
        return select_from("user.db", "users", "email", username, "username")

db.commit()
db.close()
