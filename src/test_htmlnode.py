import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_a(self):
        node = HTMLNode("a", "this is an a tag", props={"href": "https://example.com"})
        self.assertEqual(str(node), "HTMLNode(a, this is an a tag, None, {'href': 'https://example.com'})")
    
    def test_props_to_html(self):
        node = HTMLNode("a", "this is an a tag", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://example.com" target="_blank" ')

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        from htmlnode import LeafNode
        node = LeafNode("p", "This is a paragraph", props={"class": "text"})
        self.assertEqual(node.to_html(), '<p class="text" >This is a paragraph</p>')
    
    def test_to_html_no_value(self):
        from htmlnode import LeafNode
        node = LeafNode("p", None, props={"class": "text"})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_a(self):
        from htmlnode import LeafNode
        node = LeafNode("a", "Click here", props={"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com" >Click here</a>')

    def test_to_html_no_props(self):
        from htmlnode import LeafNode
        node = LeafNode("h1", "Header Text")
        self.assertEqual(node.to_html(), '<h1 >Header Text</h1>')