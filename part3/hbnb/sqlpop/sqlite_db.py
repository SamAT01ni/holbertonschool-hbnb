import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

with open("tablegen.sql") as f:
    cursor.executescript(f.read())

with open("initialize.sql") as f:
    cursor.executescript(f.read())

with open("CRUD.sql") as f:
    sql = f.read()

for statement in sql.split(";"):
    statement = statement.strip()
    if not statement:
        continue
    cursor.execute(statement)
    if statement.upper().startswith("SELECT"):
        print(statement.splitlines()[0])
        for row in cursor:
            print(" ", row)

conn.commit()
conn.close()