import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_a(self):
        node = HTMLNode("a", "this is an a tag", props={"href": "https://example.com"})
        self.assertEqual(str(node), "HTMLNode(a, this is an a tag, None, {'href': 'https://example.com'})")
    
    def test_props_to_html(self):
        node = HTMLNode("a", "this is an a tag", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://example.com" target="_blank" ')

