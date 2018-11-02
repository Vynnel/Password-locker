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

    