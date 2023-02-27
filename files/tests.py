import sqlite3
from StringSort import StringSort

class DataBase:

    def __init__(self, database):
        self.database = database

        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def new_account(self, name, password):
        self.name = name
        self.password = password

        self.connection.execute("""
            INSERT INTO "Signs" VALUES
                (?, NULL, NULL, NULL, NULL, NULL, ?)
        """, [self.name, self.password])

        self.connection.commit()

    def check_for_account(self, name, password):
        self.cursor.execute("""
            SELECT "password" FROM "Signs" WHERE "name" = ?
        """, [name])

        real_password = self.cursor.fetchall()

        if str(real_password) != '[]':
            s = StringSort(str(real_password))
            real_password2 = s.delete("[(',)]")
            if real_password2 == password:
                return True
            else:
                return False
        else:
            return False

    def get_number(self, number, name):
        if int(number) == 1:
            self.cursor.execute("""
                        SELECT "first" FROM "Signs" WHERE "name" = ?
                    """, [str(name)])

            self.info = self.cursor.fetchall()
            s = StringSort(str(self.info))
            return s.delete("[(',)]")
        if int(number) == 2:
            self.cursor.execute("""
                        SELECT "second" FROM "Signs" WHERE "name" = ?
                    """, [str(name)])

            self.info = self.cursor.fetchall()
            s = StringSort(str(self.info))
            return s.delete("[(',)]")
        if int(number) == 3:
            self.cursor.execute("""
                        SELECT "third" FROM "Signs" WHERE "name" = ?
                    """, [str(name)])

            self.info = self.cursor.fetchall()
            s = StringSort(str(self.info))
            return s.delete("[(',)]")
        if int(number) == 4:
            self.cursor.execute("""
                        SELECT "fourth" FROM "Signs" WHERE "name" = ?
                    """, [str(name)])

            self.info = self.cursor.fetchall()
            s = StringSort(str(self.info))
            return s.delete("[(',)]")
        if int(number) == 5:
            self.cursor.execute("""
                        SELECT "fifth" FROM "Signs" WHERE "name" = ?
                    """, [str(name)])

            self.info = self.cursor.fetchall()
            s = StringSort(str(self.info))
            return s.delete("[(',)]")

    def update(self, number, name, what):
        if int(number) == 1:
            self.connection.execute("""
                        UPDATE "Signs" set "first" = ? WHERE "name" = ?
                    """, [str(what), str(name)])

            self.connection.commit()
        if int(number) == 2:
            self.connection.execute("""
                                    UPDATE "Signs" set "second" = ? WHERE "name" = ?
                                """, [str(what), str(name)])

            self.connection.commit()
        if int(number) == 3:
            self.connection.execute("""
                                    UPDATE "Signs" set "third" = ? WHERE "name" = ?
                                """, [str(what), str(name)])

            self.connection.commit()
        if int(number) == 4:
            self.connection.execute("""
                                    UPDATE "Signs" set "fourth" = ? WHERE "name" = ?
                                """, [str(what), str(name)])

            self.connection.commit()
        if int(number) == 5:
            self.connection.execute("""
                                    UPDATE "Signs" set "fifth" = ? WHERE "name" = ?
                                """, [str(what), str(name)])

            self.connection.commit()

db = DataBase('database.db')