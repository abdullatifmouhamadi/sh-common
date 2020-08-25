
from sh import mysqldump, cp, mysql#, docker


class MYSQLConnection:
    def __init__(self, db_host, db_user, db_password):
        self.dbhost     = db_host
        self.dbuser     = db_user
        self.dbpassword = db_password


    def execute(self, statement):
        return mysql("-h", self.dbhost ,"-u",  self.dbuser, "-p" + self.dbpassword , "-e", "{}".format( statement ) )


    def newuserdb(self, db_name, user_password):
        self.execute(statement = "CREATE DATABASE IF NOT EXISTS {}".format(db_name))
        self.execute(statement = "CREATE USER IF NOT EXISTS '{}'@'{}' IDENTIFIED BY '{}';".format(db_name, self.dbhost, user_password))
        self.execute(statement = "GRANT ALL PRIVILEGES ON {}.* TO '{}'@'{}';".format(db_name, db_name, self.dbhost))
        self.execute(statement = "FLUSH PRIVILEGES;")
        return True




