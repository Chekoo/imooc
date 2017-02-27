class PersonDataBase(object):
    def __init__(self):
        self.__personDataBase = [('user1', 1), ('user2', 2)]
    def login(self, userName, userPassword):
        if (userName, userPassword) not in self.__personDataBase:
            print 'sorry, error'
            return None
        else:
            print 'ok'

if __name__ == "__main__":
    oneObj = PersonDataBase()
    oneObj.login('test', 1)
    oneObj.login('user1', 1)

