import unittest
from credentials import Credential


class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours
    """

    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_credential = Credential("rock1ville", "Instagram", "Vynnel", "rock1ville")

    def tearDown(self):
        """
        tearDown method that cleans up after each test has run 
        """
        Credential.credential_list = []
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.view_password, "rock1ville")
        self.assertEqual(self.new_credential.account, "Instagram")
        self.assertEqual(self.new_credential.login, "Vynnel")
        self.assertEqual(self.new_credential.password, "rock1ville")

    def test_save_credential(self):
        """
        test_save_credential test case to test if the credential object is saves into
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

   
