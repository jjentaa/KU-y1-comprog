ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'Ad31n15Tr@t012'

username = input('Username: ')
password = input('Password: ')

if(username==ADMIN_USERNAME and password==ADMIN_PASSWORD):
    print('Welcome, admin.')
else:
    print('You are not admin.')