permitted_role = ['admin']


def check_access(args):
    def wrapper(func):
        try:
            if args != 'admin':
                raise PermissionError
        except PermissionError as err:
            print(f"Error {err}: Access denied for user '{args}'")
        else:
            print(func())
    return wrapper


#@check_access('admin')
#def user_login():
    #return "Добро пожаловать"


#print(user_login())


@check_access('user')
def user_login():
    print("Добро пожаловать")


#user_login()
