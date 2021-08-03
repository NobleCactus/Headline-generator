from unittest import TestCase
from HeadlineGenerator import generate_headline

class Test(TestCase):
    def test_generate_headline(self):
        self.assertFalse(generate_headline())
