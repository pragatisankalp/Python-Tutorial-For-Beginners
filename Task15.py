''''Suppose we have user dictionary that stores the user's information like this

user={
'Id': 1,
'name': 'Pragati',
'role':'DBA',
}

We want to build a decorator check_permission() that checks the user's role and only allows
'DBA' to delete database.If user is not DBA then it print 'I am not admin'

Suppose we have  function delete_database() that can delete our whole database and decorate original function with decorator.'''

user={
'Id': 1,
'name': 'Pragati',
'role':'',
}

def check_permission(func):
    def inner():
        if user.get('role')=='DBA':
            return func()
        print('I am not admin')
    return inner

@check_permission
def delete_database():
    print('deleted database')

delete_database()