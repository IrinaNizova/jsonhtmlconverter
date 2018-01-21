import unittest
from __init__ import convert_json_to_html


class TestStringMethods(unittest.TestCase):

    def test_simple_convert(self):
        self.assertEqual(convert_json_to_html(tags=('h1', 'p')),
            "<h1>Title #1</h1><p>Hello, World 1!</p><h1>Title #2</h1><p>Hello, World 2!</p>")


    def test_custom_tags_convert(self):
        self.assertEqual(convert_json_to_html(tags=('h3', 'div')),
            "<h3>Title #1</h3><div>Hello, World 1!</div><h3>Title #2</h3><div>Hello, World 2!</div>")


if __name__ == '__main__':
    unittest.main()