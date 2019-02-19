
import hashlib


class User(object):
    '''This class will handle creation, management,
    and other functionality of user accounts'''

    def __init__(self, *args, **kwargs):
        '''requires pin, name can resort to default'''
        self._name = kwargs.get('name', User.default())
        self.hash = hashlib.sha256()
        self._pin = self.encrypt(kwargs.get('pin', None))

        if self.pin is None:
            return 'No pin specified'

    def encrypt(self, pin):
        '''encrypts the pin to SHA256 hash'''
        hashed = self.hash.update(bytes(pin))
        return hashed.digest()

    def verify(self, pin):
        '''Verifies SHA256 Hash'''
        if self.encrypt(pin) == self.pin:
            return True
        else:
            return False

    def login(self, *args, **kwargs):
        '''attempts to login user using verify method'''
        name = kwargs.get('name', None)
        pin = kwargs.get('pin', None)
        if self.verify(pin):
            return True
        else:
            return False

    def change_name(self, name):
        '''changes name of user'''
        self.name = name

    @classmethod
    def default(cls):
        return 'default'

    # name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    # pin property
    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, value):
        self._pin = value


class Account(object):

    def __init__(self, *args, **kwargs):
        pass


class Authenticator(object):
    '''This class will handle authintcation
    of information between user and client'''
    pass


class Exceptions:
    pass

