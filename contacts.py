import pymysql

class Contacts():

    def __init__(self):
        print('             Bienvenidos a mi programa, podrás guardar a tus contactos (clientes en esta agenda)')


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
        self.connection() #invocamos nuestra conexion con la db
        name = str(input('Ingresa tu nombre: '))
        last_name = str(input('Ingresa tu apellido: '))
        email = str(input('Ingresa tu correo: '))

        try:
            query = "INSERT INTO usuarios(nombre, apellido, correo) VALUES('{}','{}','{}')".format(name, last_name, email)

            self.close_db(query) #en esta función se encuentra execute, commit y close

        except Exception as e:
            print('Intenta nuevamente')


    def update_user(self):
        self.connection()
        name = str(input('Ingresa el nombre de la persona que deseas actualizar: '))
        if self.select_user(name):
            #si el usuario existe, entonces lo actualizamos
            name = str(input('Ingresa tu nombre: '))
            last_name = str(input('Ingresa tu apellido: '))
            email = str(input('Ingresa tu correo: '))

            query = "UPDATE usuarios SET nombre='{}', apellido='{}',correo='{}' WHERE usuario_id={}".format(name, last_name, email, self.users[0])

            self.close_db(query)


    def delete_user(self):
        self.connection()
        name = str(input('Ingresa el nombre de la persona que deseas eliminar: '))
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
            print('NOMBRE:', self.users[1])
            print('APELLIDO:', self.users[2])
            print('CORREO:', self.users[3])
            #si se ejecuta esta ultima linea, es porque el usuario existe por lo tanto
            #se puede modificar o eliminar.
            return True
        except Exception as e:
            print('El usuario no existe')


    def show_all(self):
        self.connection()
        query = "SELECT * FROM usuarios"

        try:
            self.cursor.execute(query)
            #users = self.cursor.fetchall()
            # for user in users:
            #     print('ID:', user[0])
            #     print('NOMBRE:', user[1])
            #     print('APELLIDO:', user[2])
            #     print('CORREO:', user[3])

            for user in self.cursor.fetchall():
                print('-----*-----*-----*-----*----*-----*-----*')
                print(f'NOMBRE: {user[1]}, APELLIDO: {user[2]}, CORREO: {user[3]}')
                print('-----*-----*-----*-----*----*-----*-----*')

        except Exception as e:
            print(e, 'El usuario no existe')

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

        command = str(input("""Que deseas hacer
                 [i]nsertar
                 [a]ctualizar
                 [e]liminar
                 [b]uscar
                 [s]alir: """))

        if command == 'i':
            con.insert_user()
        elif command == 'a':
            con.update_user()
        elif command == 'e':
            con.delete_user()
        elif command == 'b':
            name = str(input('Ingresa el nombre que deseas buscar: '))
            con.select_user(name)
        elif command == 's':
            print('Vuelva pronto')
            break
        else:
            print('Ingresa un comando válido')
