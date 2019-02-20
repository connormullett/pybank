
import unittest
from pybank.models import User, Account, AccountTypes


class TestUserModel(unittest.TestCase):

    def test_init_should_create_user_given_correct_args(self):
        self.user = User(name='Connor', pin=1234)
        self.assertIsInstance(self.user, User)

    def test_init_should_raise_value_error_given_incorrect_pin(self):
        with self.assertRaises(ValueError):
            user = User(name='Connor', pin=12345)


    def test_init_should_assign_default_name_if_name_not_given(self):
        self.user = User(pin=1234)
        self.assertTrue(self.user.name == 'default')

    def test_init_should_raise_value_error_given_no_pin(self):
        with self.assertRaises(ValueError):
            user = User(name='Connor')

    def test_verify_should_return_true_with_correct_values(self):
        self.user = User(pin=1234, name='Connor')
        self.assertTrue(self.user.verify(1234))

    def test_verify_should_return_false_with_incorrect_pin(self):
        self.user = User(pin=1234, name='Connor')
        self.assertFalse(self.user.verify(1235))

    def test_login_should_return_true_if_correct_info(self):
        self.user = User(pin=1234, name='Connor')
        self.assertTrue(self.user.login(name='Connor', pin=1234))

    def test_login_should_return_false_if_incorrect_pin(self):
        self.user = User(pin=1234, name='Connor')
        self.assertFalse(self.user.login(name='Connor', pin=1253))

    def test_login_should_return_false_if_incorrect_name(self):
        self.user = User(pin=1234, name='Connor')
        self.assertFalse(self.user.login(name='jimmy', pin=1234))

    def test_change_name_should_change_name_with_correct_info(self):
        self.user = User(pin=1234, name='Connor')
        self.assertTrue(self.user.change_name(name='connor jr', pin=1234))
        self.assertTrue(self.user.name == 'connor jr')

    def test_change_name_should_return_false_with_incorrect_pin(self):
        self.user = User(pin=1234, name='Connor')
        self.assertFalse(self.user.change_name(name='connor', pin=1235))

    def test_change_pin_should_change_pin(self):
        self.user = User(pin=1234, name='Connor')
        self.assertTrue(self.user.change_pin(1235, 1234))

    def test_change_pin_should_return_false_with_incorrect_pin(self):
        self.user = User(pin=1234, name='Connor')
        self.assertFalse(self.user.change_pin(1243, 1243))

    def test_encrypt_should_return_hex_digest(self):
        self.user = User(pin=1234, name='Connor')
        actual = self.user._encrypt(1234)
        expected = self.user.pin
        self.assertEqual(actual, expected)

    def test_add_account_should_create_account(self):
        self.user = User(pin=1234, name='Connor')
        self.user.add_account(pin=1234, account_type=1)
        self.assertTrue(self.user.account)

    def test_add_account_should_return_none(self):
        self.user = User(pin=1234, name='Connor')
        self.assertIsNone(self.user.add_account(pin=1235, account_type=1))

    # TODO: Test properties

class TestAccountModel(unittest.TestCase):

    def test_init_should_return_created_instance_with_good_credentials(self):
        pass

    def test_init_should_return_false_if_user_cant_be_verified(self):
        pass

