import pymysql

class Contacts():

    def __init__(self):
        print('             Welcome to your agenda 2.0, you can save all your contacts!')


    def connection(self):
        #start connection
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='agenda'
        )

        self.cursor = self.db.cursor()


    def insert_user(self):
        self.connection() #start a connection with database
        name = str(input('Type your name: '))
        last_name = str(input('Type your last name: '))
        email = str(input('Type your email: '))

        try:
            query = "INSERT INTO users(name, last_name, email) VALUES('{}','{}','{}')".format(name, last_name, email)

            self.close_db(query) #in this function there are commands: execute, commit and close

        except Exception as e:
            print('Please, try again!')


    def update_user(self):
        self.connection()
        name = str(input('Type name to update: '))
        if self.select_user(name):
            #if user exist, then update row
            name = str(input('Type your name: '))
            last_name = str(input('Type yout last name: '))
            email = str(input('Type your email: '))

            query = "UPDATE users SET name='{}', last_name='{}',email='{}' WHERE user_id={}".format(name, last_name, email, self.users[0])

            self.close_db(query)


    def delete_user(self):
        self.connection()
        name = str(input('Type name to delete: '))
        if self.select_user(name):
            query = "DELETE FROM users WHERE user_id={}".format(self.users[0])

            self.close_db(query)


    def select_user(self, name):
        self.connection()
        query = "SELECT * FROM users WHERE name = '{}'".format(name)

        try:
            self.cursor.execute(query)

            # mediante el método fetchone, el resultado se asigna a la variable
            # self.users, entonces esta variable obtendra todo un registro, en este caso
            # son 4 campos, entonces los imprimimos de la siguiente manera.

            self.users = self.cursor.fetchone()
            print('ID:', self.users[0])
            print('NAME:', self.users[1])
            print('LAST NAME:', self.users[2])
            print('EMAIL:', self.users[3])
            #si se ejecuta esta ultima linea, es porque el usuario existe por lo tanto
            #se puede modificar o eliminar.
            return True
        except Exception as e:
            print("The user doesn't exist")


    def show_all(self):
        self.connection()
        query = "SELECT * FROM users"

        try:
            self.cursor.execute(query)
            #another way to show de users
            #users = self.cursor.fetchall()
            # for user in users:
            #     print('ID:', user[0])
            #     print('NAME:', user[1])
            #     print('LAST NAME:', user[2])
            #     print('EMAIL:', user[3])

            for user in self.cursor.fetchall():
                print('-----*-----*-----*-----*----*-----*-----*')
                print(f'NAME: {user[1]}, LAST NAME: {user[2]}, EMAIL: {user[3]}')
                print('-----*-----*-----*-----*----*-----*-----*')

        except Exception as e:
            print(e, "The user doesn't exist")

    def close_db(self, query):
        #execute sql
        self.cursor.execute(query)
        #confirm the sql
        self.db.commit()
        #show new rows
        self.show_all()
        #close connection
        self.db.close()