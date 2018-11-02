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
        tearDown method that does clean up after each test case has run
        """
        Credential.credential_list = []

   