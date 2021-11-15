"""

    Decorator:
        decorator pattern != python decorator

"""



class Article:
    def show_all_articles(self):
        print('all article ...')


# Permission
class Login:
    def check_login(self, username, password):
        if username == 'Admin' and password == '123456':
            return True

# Decorator
def login_required(function):
    def check_login():
        username = str(input('Enter username: '))
        password = str(input('Enter password: '))
        check_user = Login()
        result = check_user.check_login(username, password)
        if result:
            function()
        else: 
            print('No Access')
    return check_login



# access article
@login_required
def get_article():
    articles = Article()
    articles.show_all_articles()


get_article()

