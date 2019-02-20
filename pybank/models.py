
import hashlib

from enum import Enum


class User(object):
    '''This class will handle creation, management,
    and other functionality of user accounts'''

    user_id = 0

    def __init__(self, *args, **kwargs):
        '''requires pin, name can resort to default'''
        self._name = kwargs.get('name', User.default())
        self._user_id = User.generate_id()

        if len(str(kwargs.get('pin', None))) == 4:
            self._pin = self.encrypt(kwargs.get('pin', None))
        else:
            raise ValueError('Pin must be 4 digits long')
        if self.pin is None:
            raise ValueError('No Pin specified')

    def add_account(self, *args, **kwargs):
        '''
        creates an account instance and binds to the user
        :params: pin, account_type: int (see AccountTypes Enumeration)
        '''
        pin = kwargs.get('pin', None)
        account_type = kwargs.get('account_type', None)
        if self.verify(pin) and account_type is not None:
            return Account(account_type=account_type, user_id=self.user_id)
        return None

    def encrypt(self, pin):
        '''encrypts the pin to SHA256 hash'''
        h = hashlib.sha256(bytes(pin))
        return h.digest()

    def verify(self, pin):
        '''Verifies SHA256 Hash'''
        if self.encrypt(pin) == self.pin:
            return True
        return False

    def login(self, *args, **kwargs):
        '''attempts to login user using verify method'''
        name = kwargs.get('name', None)
        pin = kwargs.get('pin', None)
        if self.verify(pin):
            return True
        else:
            return False

    def change_name(self, name, pin):
        '''changes name of user'''
        if self.verify(pin):
            self.name = name
            return self.name
        else:
            return None

    def change_pin(self, new_pin, old_pin):
        '''Attempts to change pin of user
           params: new_pin, old_pin
           returns: True or False'''
        if self.verify(old_pin):
            self.pin = self.encrypt(new_pin)
            return True
        else:
            return False

    @classmethod
    def default(cls):
        return 'default'

    @classmethod
    def generate_id(cls):
        User.user_id += 1
        return User.user_id

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

    # id property, no setter
    @property
    def user_id(self):
        return self._user_id


class AccountTypes(Enum):
    CHECKING = 1
    SAVING = 2


class Account(object):
    '''this class will handle manipulations of
       account instances'''

    _account_id = 0

    def __init__(self, *args, **kwargs):
        '''
        params: user_id: int, account_type: int
        '''
        self._user_id = kwargs.get('user_id', None)

        account_type = kwargs.get('account_type', None)
        self._account_id = Account.get_account_id()

        if account_type:
            self._account_type = AccountTypes(account_type)
        else:
            raise ValueError('account_type cannot be None')
        if not self.user_id:
            raise ValueError('user_id cannot be None')

    @classmethod
    def get_account_id(cls):
        Account._account_id += 1
        return Account._account_id

    def deposit(self, *args, **kwargs):
        pass

    def withdraw(self, *args, **kwargs):
        pass

    def get_balance(self, *args, **kwargs):
        pass


class Exceptions:
    '''
    This class may be a throw away, used for any new exceptions
    needed for this library
    '''
    pass

