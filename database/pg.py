import psycopg2

class PGSQLConnection:
    def __init__(self):
        """

        """

    def create_user_with_createdb(self, name, password):
        try:
            r = self.executepg(statement = "CREATE USER {} WITH ENCRYPTED PASSWORD '{}' CREATEDB;".format(name, password))
            return r
        except psycopg2.errors.DuplicateObject:
            return "role already exists"


    def executepg(self, statement):
        db = psycopg2.connect(
            host    = 'localhost', 
            port    = 5432, 
            user    = 'postgres', 
            database= 'postgres'
        )
        db.autocommit = True
        cur = db.cursor()
        r = cur.execute( statement )
        return r
        #print(cur)


