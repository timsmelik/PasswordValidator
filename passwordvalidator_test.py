import unittest

from passwordvalidator import *

class PasswordValidatorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.pv = PasswordValidator()

    @classmethod
    def tearDownClass(cls):
        del cls.pv

    def testValidPassword(self):
        password = 'ValidPassword1!'
        result = self.pv.validate(password)
        self.assertTrue(result['success'])
        self.assertTrue(len(result['errors']) == 0)

    def testShortPassword(self):
        password = 'Sh1!'
        result = self.pv.validate(password)
        self.assertFalse(result['success'])
        self.assertTrue(len(result['errors']) == 1)

    def testMissingDigit(self):
        password = 'MissingDigit!'
        result = self.pv.validate(password)
        self.assertFalse(result['success'])
        self.assertTrue(len(result['errors']) == 1)

    def testMissingUppercase(self):
        password = 'missinguppercase1!'
        result = self.pv.validate(password)
        self.assertFalse(result['success'])
        self.assertTrue(len(result['errors']) == 1)

    def testMissingLowerCase(self):
        password = 'MISSINGLOWERCASE1!'
        result = self.pv.validate(password)
        self.assertFalse(result['success'])
        self.assertTrue(len(result['errors']) == 1)

    def testEmptyString(self):
        password = ''
        result = self.pv.validate(password)
        self.assertFalse(result['success'])
        self.assertTrue(len(result['errors']) == 5)
