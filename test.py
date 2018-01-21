import unittest
from __init__ import convert_json_to_html


class TestStringMethods(unittest.TestCase):

    def test_simple_convert(self):
        self.assertEqual(convert_json_to_html(tags=('h1', 'p')),
            "<ul><li><h1>Title #1</h1><p>Hello, World 1!</p></li>"
            "<li><h1>Title #2</h1><p>Hello, World 2!</p></li></ul>")


    def test_custom_tags_convert(self):
        self.assertEqual(convert_json_to_html(tags=('h3', 'div')),
            "<ul><li><h3>Title #1</h3><div>Hello, World 1!</div></li>"
            "<li><h3>Title #2</h3><div>Hello, World 2!</div></li></ul>")


if __name__ == '__main__':
    unittest.main()