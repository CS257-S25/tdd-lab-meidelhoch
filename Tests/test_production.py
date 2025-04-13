import sys
import unittest
from io import StringIO
from production import reverse_word, reverse_all_words, main


class TestReverseWord(unittest.TestCase):
    '''
	Tests for the reverse_word function.
	'''
    def test_reverse(self):
        self.assertEqual(reverse_word("superman"),
                         "namrepus", "Should be namrepus")
        self.assertEqual(reverse_word("octopus"),
                         "supotco", "Should be supotco")
        self.assertEqual(reverse_word("a"), "a", "Should be a")
        self.assertEqual(reverse_word("Hello"), "olleH", "Should be olleH")
        self.assertEqual(reverse_word(""), "", "Should be empty")


class TestReverseAllWords(unittest.TestCase):
    '''
	Tests for the reverse_all_words function.
	'''
    def test_reverse_all_words(self):
        self.assertEqual(reverse_all_words("superman octopus"),
                         "namrepus supotco", "Should be namrepus supotco")
        self.assertEqual(reverse_all_words("a B c"),
                         "a B c", "Should be a B c")
        self.assertEqual(reverse_all_words("hello world"),
                         "olleh dlrow", "Should be olleh dlrow")
        self.assertEqual(reverse_all_words("Whatever"),
                         "revetahW", "Should be revetahW")
        self.assertEqual(reverse_all_words("this is a test"),
                         "siht si a tset", "Should be siht si a tset")
        self.assertEqual(reverse_all_words(""), "", "Should be empty")


class TestReverseUserInput(unittest.TestCase):
    '''
	Tests for taking in command line input and reversing it.
	'''
    def test_reverse_user_input(self):
        sys.argv = ['production.py', 'this is a test']
        sys.stdout = StringIO()
        main()
        printed_output = sys.stdout.getvalue()
        self.assertEqual(printed_output, "siht si a tset\n",
                         "Should be siht si a tset\n")

        sys.argv = ['production.py']
        sys.stdout = StringIO()
        main()
        printed_output = sys.stdout.getvalue()
        self.assertEqual(printed_output, "Please provide a string to reverse.\n",
                         "Should be Please provide a string to reverse.\n")
