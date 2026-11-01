# Decorator for displaying service status messages
def log(func):
    def wrapper():
        print('Checking internet connection')
        print('Checking SMS service connection')
        print('Checking SMS panel credit')

        func()

        print('Checking FluffyBanana website response')
        print('SMS delivery status')
        print('Hamrah Aval operator delivery status')
        print('User delivery status')
        print(30 * '=')

    return wrapper


# User registration
@log
def login():
    print('Your registration was completed successfully')


login()


# Payment process
@log
def payment():
    print('Payment completed successfully')


payment()