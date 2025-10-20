import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):

    def test_extract_title_success(self):
        markdown = "# This is the Title\n\nSome content here."
        title = extract_title(markdown)
        self.assertEqual(title, "This is the Title")

    def test_extract_title_no_title(self):
        markdown = "No title here, just content."
        with self.assertRaises(ValueError) as context:
            extract_title(markdown)
        self.assertEqual(str(context.exception), "No title found in markdown")