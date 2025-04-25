import unittest
import re
from enum import Enum, auto
from textnode import *
from text_types import TextNode, TextType
from split_delimiter import *
from htmlnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_equal_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_equal_different_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_equal_different_url(self):
        node = TextNode("This is a text node", TextType.LINK, "https://example.com")
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.LINK, "https://example.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://example.com")
        self.assertEqual(node, node2)


class TestTexttoTextNode(unittest.TestCase):
	def test_all_types(self):
		text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
		result = text_to_textnodes(text)

		self.assertEqual(10, len(result))

		self.assertEqual(TextNode("This is ", TextType.TEXT), result[0])
		self.assertEqual(TextNode("text", TextType.BOLD), result[1])
		self.assertEqual(TextNode(" with an ", TextType.TEXT), result[2])
		self.assertEqual(TextNode("italic", TextType.ITALIC), result[3])
		self.assertEqual(TextNode(" word and a ", TextType.TEXT), result[4])
		self.assertEqual(TextNode("code block", TextType.CODE), result[5])
		self.assertEqual(TextNode(" and an ", TextType.TEXT), result[6])
		self.assertEqual(TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"), result[7])
		self.assertEqual(TextNode(" and a ", TextType.TEXT), result[8])
		self.assertEqual(TextNode("link", TextType.LINK, "https://boot.dev"), result[9])



if __name__ == "__main__":
    unittest.main()

