'''have a simple add function, but this add function
only executes if the credentials are valid
'''
valid_creds={'user_name':'test', 'password':'test123'}

def wrapper(u, p):
    def credential_checker(func):
        def inner(a,b):
            file_handle = open('INTERVIEW_PROBLEMS\input_file.txt','r')
            data = file_handle.read()
            username = data.split(',')[0]
            password = data.split(',')[1]

            username = u
            password = p

            if username == valid_creds['user_name'] and password == valid_creds['password']:
                print('creds valid... executing function...')
                return func(a,b)
            else:
                return ('credentials invalid')
        return inner
    return credential_checker


@wrapper('test','test1234')
def add_numbers(a,b):
    return a+b

print(add_numbers(1,2))