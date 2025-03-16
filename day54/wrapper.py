class user:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def authnticator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@authnticator
def create_blog(user):
    return f"This is {user.name}'s blog"

new_user = user('Ankush')
new_user.is_logged_in = True
print(create_blog(new_user))