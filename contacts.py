from agenda import Contacts

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
            print('See you later!, Thanks for use Agenda')
            break
        else:
            print('Type a correct option')
