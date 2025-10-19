import unittest
from block import BlockType, block_to_block_type

class TestBlock(unittest.TestCase):

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)

    def test_heading(self):
        self.assertEqual(block_to_block_type("# This is a heading"), BlockType.HEADING)

    def test_code(self):
        self.assertEqual(block_to_block_type("```\nprint('Hello, world!')\n```"), BlockType.CODE)

    def test_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2\n- Item 3"), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. Item 1\n2. Item 2\n3. Item 3"), BlockType.ORDERED_LIST)
