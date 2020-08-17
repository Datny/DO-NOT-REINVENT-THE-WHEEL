import unittest
from unittest.mock import patch

from main import get_title, get_books_by_title


TITLE_1 = "Blarg1 Sumo"
YES = "Y"
NO = "N"


class TestBookMethods(unittest.TestCase):

    @patch('builtins.input', side_effect=[TITLE_1, YES])
    def test_get_title(self, mock_input):
        self.assertEqual(get_title(), TITLE_1)

    #TODO: Remember to put it also in integration tests
    def test_get_books_by_title(self):
        pass


if __name__ == '__main__':
    unittest.main()
