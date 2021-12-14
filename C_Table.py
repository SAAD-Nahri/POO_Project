import sqlite3


class C_Table():
    dbname = "database.db"
    conn = sqlite3.connect(dbname)
    @classmethod
    def is_table(cls):
        with cls.conn:
            query = "SELECT name from sqlite_master WHERE type='table' AND name='{" + cls.__name__ + "}';"
            cursor = cls.conn.execute(query)
            result = cursor.fetchone()
            if result:
                return False
            else:
                return True
    @classmethod
    def create_table(cls):
        with cls.conn:
            c = cls.conn.cursor()
            a = "CREATE TABLE if not exists "+cls.__name__+" ("
            for attribute, value in cls.A.items():
                a = a + str(attribute) + " " + str(value) + ","
            a = a[:len(a) - 1] + ")"
            c.execute(a)

    @classmethod
    def tuple_to_obj(cls, a):
        e = cls()
        for K in range(len(a)):
            setattr(e, list(e.A.keys())[K], a[K])
        return e


    @classmethod
    def get_all_obj(cls, **kwargs):
        b = []
        for elem in cls.all_etudient_filtter(**kwargs):
            b.append(cls.tuple_to_obj(elem))
        return b

    def affiche_elem(self):
        i = 0
        for attribute, value in self.__dict__:
            print(f"{i}-{attribute}: {value}")
            i += 1

    def save(self):
        with self.conn:
            c = self.conn.cursor()
            s = f"REPLACE INTO {self.__class__.__name__} VALUES ("
            for i in range(len(self.A)):
                s = s + "?" + ","
            s = s[:len(s) - 1] + ")"
            c.execute(s, tuple(self.__dict__.values()))
    @classmethod
    def all_etudient_filtter(cls,**kwargs):
        with cls.conn:
            if kwargs:
                query = "SELECT * from "+cls.__name__+" WHERE ("
                s = ")=("
                for elem in kwargs.keys():
                    query = query + str(elem) + ","
                    s = s + "?" + ","
                query = query[:len(query) - 1] + s[:len(s) - 1] + ")"
                cursor = cls.conn.execute(query, tuple(kwargs.values()))
            else:
                query = f"SELECT * from {cls.__name__} ;"
                cursor = cls.conn.execute(query)
            return cursor.fetchall()
    @classmethod
    def update_elem(cls,**kwargs):
        with cls.conn:
            w = f") WHERE {list(kwargs.keys())[0]} = ({kwargs[list(kwargs.keys())[0]]})"
            query = f"UPDATE {cls.__name__} SET ("
            S = ")=("
            del kwargs[list(kwargs.keys())[0]]
            for elem in kwargs.keys():
                query = query + str(elem)+","
                S = S + "?" + ","
            query = query[:len(query) - 1] + S[:len(S) - 1] + w
            cls.conn.execute(query, tuple(kwargs.values()))


    @classmethod
    def update_elem1(cls,**kwargs):
        elem = cls.all_etudient_filtter(**kwargs)
        if elem:
            a = cls.get_all_obj(**kwargs)[0]
            a.sasier_Etudient(*elem)
            a.save()
        else:
            print("ce Etudient ne pas existe")

    @classmethod
    def remove_elem(cls, **kwargs):
        with cls.conn:
            cls.conn.execute(f"DELETE from {cls.__name__} WHERE ({list(kwargs.keys())[0]}) = (?)",(kwargs[list(kwargs.keys())[0]],))

