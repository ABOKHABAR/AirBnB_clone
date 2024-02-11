#!/usr/bin/python3
import unittest
from models.state import State
"""Module name = State class
"""


class TestUser(unittest.TestCase):
    ''' Unittest is tr for Stateasdsaidjia class '''

    def test_object_Instantiation(self):
        ''' instantiateasdadasdas classdsoajdsoijdisad '''
        self.state = State()

    def testattr(self):
        ''' test Class: Statesadsadsdawdsaod attributes '''
        self.state = State()
        self.assertTrue(hasattr(self.state, "today"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertFalse(hasattr(self.state, "random_attr"))
        self.assertTrue(hasattr(self.state, "mossab"))
        self.assertTrue(hasattr(self.state, "2024"))
        self.assertEqual(self.state.name, "")
        self.state.name = "abokhabar"
        self.assertEqual(self.state.name, "abokhabar")
        self.assertEqual(self.state.__class__.__name__, "State")

    def testsave(self):
        ''' testing method: savesdiajsidhsa9iuhdiusad '''
        self.state = State()
        self.state.save()
        self.assertTrue(hasattr(self.state, "updated_at"))

    def teststr(self):
        ''' testinsadsdag __str__ rsadsadadsadasdeturn format of BaseModel '''
        self.state = State()
        s = "[{}] ({}) {}".format(self.state.__class__.__name__,
                                  str(self.state.id), self.state.__dict__)
        self.assertEqual(print(s), print(self.state))

if __name__ == '__main__':
    unittest.main()
