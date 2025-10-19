import unittest
from extract_markdown import extract_markdown_images, extract_markdown_link

class TestExtractMarkdownImages(unittest.TestCase):
    def test_single_image(self):
        text = "Here is an image: ![alt text](image1.png)"
        images = extract_markdown_images(text)
        self.assertListEqual(images, [("alt text", "image1.png")])

    def test_multiple_images(self):
        text = "Images: ![img1](img1.jpg) and ![img2](img2.png)"
        images = extract_markdown_images(text)
        self.assertListEqual(images, [('img1', 'img1.jpg'), ('img2', 'img2.png')])

    def test_no_images(self):
        text = "This text has no images."
        images = extract_markdown_images(text)
        self.assertListEqual(images, [])

    def test_malformed_image_syntax(self):
        text = "This is not an image: ![alt text(image3.png"
        images = extract_markdown_images(text)
        self.assertListEqual(images, [])

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_single_link(self):
        text = "Here is a link: [example](http://example.com)"
        links = extract_markdown_link(text)
        self.assertListEqual(links, [("example", "http://example.com")])

    def test_multiple_links(self):
        text = "Links: [Google](http://google.com) and [OpenAI](http://openai.com)"
        links = extract_markdown_link(text)
        self.assertListEqual(links, [('Google', 'http://google.com'), ('OpenAI', 'http://openai.com')])

    def test_no_links(self):
        text = "This text has no links."
        links = extract_markdown_link(text)
        self.assertListEqual(links, [])

    def test_malformed_link_syntax(self):
        text = "This is not a link: [example(http://example.com"
        links = extract_markdown_link(text)
        self.assertListEqual(links, [])