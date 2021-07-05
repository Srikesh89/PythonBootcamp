'''Test file to test using_unittests.py'''
import unittest
import using_unittests

class TestUsingUnittests(unittest.TestCase):
    '''Test Methods'''
    def test_one_word(self):
        '''input: one word
            expected result: capitalized word'''
        text = 'python'
        result = using_unittests.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        '''input: two words
            expected result: two capitalized words'''
        text = 'monty python'
        result = using_unittests.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()
