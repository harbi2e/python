num_of_tries = 0
while num_of_tries != 3:
    username = input('Please insert your username: ')
    password = input('Please insert your password: ')
    if username == 'Eyad' and password == '123456':
        print('Welcome Eyad')
        num_of_tries = 0
        exit()
    else:
        print('Error')
        num_of_tries +=1
        print('You have ' + str(3 - num_of_tries) + " tries ot left")

num_of_tries = 0
while num_of_tries != 3:
    username = input('please insert your username: ')
    password = input('please insert your password: ')
    if username == 'Eyad' and password == '123456':
        print('Welcome')
        num_of_tries = 0
        exit()
    else:
        print('Error')
        num_of_tries +=1
        print(' you have ' + str(3 - num_of_tries) + " trise to lift")