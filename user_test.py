import unittest
from user import User


class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviours
    """

    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_user = User("Vynnel", "rock1ville")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.username, "Vynnel")
        self.assertEqual(self.new_user.password, "rock1ville")

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into the users' list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

   