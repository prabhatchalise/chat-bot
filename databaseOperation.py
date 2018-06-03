#####################################################################
#                                                                   #
#   Database operation of creating and inserting into table         #
#                                                                   #
#####################################################################


import sqlite3

conn = sqlite3.connect('faq.db')

c = conn.cursor()


def create_answer_table():
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS answer(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        question TEXT NOT NULL,
                                        answer TEXT NOT NULL
                                        )""")

    except sqlite3.OperationalError:
        print('Answer table could not be created.')
    c.close()


def create_subject_table():
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS subject(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    subject TEXT NOT NULL,
                                    answer_id integer NOT NULL,
                                    FOREIGN KEY(answer_id) REFERENCES answer(id)
                                    )""")

    except sqlite3.OperationalError:
        print('Subject table could not be created.')


def create_root_table():
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS root(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    root TEXT NOT NULL,
                                    answer_id integer NOT NULL,
                                    FOREIGN KEY(answer_id) REFERENCES answer(id)
                                    )""")

    except sqlite3.OperationalError:
        print('Root table could not be created.')


def create_object_table():
    try:
        c.execute("""CREATE TABLE IF NOT EXISTS object(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    object TEXT NOT NULL,
                                    answer_id integer NOT NULL,
                                    FOREIGN KEY(answer_id) REFERENCES answer(id)
                                    )""")

    except sqlite3.OperationalError:
        print('Object table could not be created.')


# Insert question along with their answer
def insert_answer(question, answer):
    try:
        c.execute("INSERT INTO answers VALUES (?,?)", (question, answer))
        conn.commit()

    except sqlite3.OperationalError:
        print('Error while inserting into answer table.')

    c.close()
    conn.close()


# Subject of the parsed question and its answer id
def insert_subject(subject, answer_id):
    try:
        c.execute("INSERT INTO subject VALUES (?,?)", (subject, answer_id))
        conn.commit()

    except sqlite3.OperationalError:
        print('Error while inserting into subject table.')


# Root of the parsed question and its answer id
def insert_root(root, answer_id):
    try:
        c.execute("INSERT INTO root VALUES (?,?)", (root, answer_id))
        conn.commit()

    except sqlite3.OperationalError:
        print('Error while inserting into subject table.')


# Object of the parsed question and its answer id
def insert_object(object, answer_id):
    try:
        c.execute("INSERT INTO object VALUES (?,?)", (object, answer_id))
        conn.commit()

    except sqlite3.OperationalError:
        print('Error while inserting into subject table.')


# gives no of row of the answer table
def no_of_rows():
    c = conn.cursor()
    n = c.execute("SELECT Count(*) FROM answer")
    c.close()
    return n



create_answer_table()
create_object_table()
create_subject_table()
create_object_table()

no_of_rows()

c.close()
conn.close()
