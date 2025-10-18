import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT, url="https://example.com")
        expected_repr = "TextNode(This is a text node, italic, https://example.com)"
        self.assertEqual(repr(node), expected_repr)

    def test_url(self):
        node = TextNode("This is a text node", TextType.LINK_TEXT, url="https://example.com")
        self.assertEqual(node.url, "https://example.com")



if __name__ == "__main__":
    unittest.main()