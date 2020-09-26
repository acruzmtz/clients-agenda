import pymysql

class Contacts():

    def __init__(self):
        print('             Welcome to your agenda, you can save all your contacts!')


    def connection(self):
        #iniciamos la conexión
        self.db = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='test'
        )

        self.cursor = self.db.cursor()


    def insert_user(self):
        self.connection() #start a connection with database
        name = str(input('Type your name: '))
        last_name = str(input('Type your last name: '))
        email = str(input('Type your email: '))

        try:
            query = "INSERT INTO usuarios(nombre, apellido, correo) VALUES('{}','{}','{}')".format(name, last_name, email)

            self.close_db(query) #en esta función se encuentra execute, commit y close

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

            query = "UPDATE usuarios SET nombre='{}', apellido='{}',correo='{}' WHERE usuario_id={}".format(name, last_name, email, self.users[0])

            self.close_db(query)


    def delete_user(self):
        self.connection()
        name = str(input('Type name to delete: '))
        if self.select_user(name):
            query = "DELETE FROM usuarios WHERE usuario_id={}".format(self.users[0])

            self.close_db(query)


    def select_user(self, name):
        self.connection()
        query = "SELECT * FROM usuarios WHERE nombre = '{}'".format(name)

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
        query = "SELECT * FROM usuarios"

        try:
            self.cursor.execute(query)
            #another way to show de users
            #users = self.cursor.fetchall()
            # for user in users:
            #     print('ID:', user[0])
            #     print('NOMBRE:', user[1])
            #     print('APELLIDO:', user[2])
            #     print('CORREO:', user[3])

            for user in self.cursor.fetchall():
                print('-----*-----*-----*-----*----*-----*-----*')
                print(f'NAME: {user[1]}, LAST NAME: {user[2]}, EMAIL: {user[3]}')
                print('-----*-----*-----*-----*----*-----*-----*')

        except Exception as e:
            print(e, "The user doesn't exist")

    def close_db(self, query):
        #ejecutamos la consulta
        self.cursor.execute(query)
        #confirmamos la consulta de sql
        self.db.commit()
        #mostramos los nuevos datos
        self.show_all()
        #cerramos la conexion
        self.db.close()

if __name__ == '__main__':
    con = Contacts()
    con.show_all()

    while True:

        command = str(input("""What do you want to do
                 [c]reate
                 [r]ead
                 [u]pdate
                 [d]elete
                 [s]ing out: """))

        if command == 'c':
            con.insert_user()
        elif command == 'u':
            con.update_user()
        elif command == 'd':
            con.delete_user()
        elif command == 'r':
            name = str(input('Type name to find: '))
            con.select_user(name)
        elif command == 's':
            print('See you later!')
            break
        else:
            print('Type a correct option')
