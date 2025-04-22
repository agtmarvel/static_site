import unittest
from textnode_to_htmlnode import *
from htmlnode import *
from textnode import TextNode, TextType

class TestTextnodeToHtmlnode(unittest.TestCase):
	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, None)
		self.assertEqual(html_node.value, "This is a text node")
	def test_bold(self):
		node = TextNode("This is bold text", TextType.BOLD)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "b")
		self.assertEqual(html_node.value, "This is bold text")
	def test_italic(self):
		node = TextNode("Italic text is fancy", TextType.ITALIC)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "i")
		self.assertEqual(html_node.value, "Italic text is fancy")
	def test_code(self):
		node = TextNode("print(Code in html, what are we Boot.dev?)", TextType.CODE)
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "code")
		self.assertEqual(html_node.value, "print(Code in html, what are we Boot.dev?)")
	def test_link(self):
		node = TextNode("Click here", TextType.LINK)
		node.url = "https://boot.dev"
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "a")
		self.assertEqual(html_node.value, "Click here")
		self.assertEqual(html_node.props["href"], "https://boot.dev")
	def test_image(self):
		node = TextNode("Alt text for image", TextType.IMAGE)
		node.url = "https://example.com/image.png"
		html_node = text_node_to_html_node(node)
		self.assertEqual(html_node.tag, "img")
		self.assertEqual(html_node.value, "")
		self.assertEqual(html_node.props["src"], "https://example.com/image.png")
		self.assertEqual(html_node.props["alt"], "Alt text for image")
	def test_invalid_type(self):
		node = TextNode("Invalid type", "not_a_valid_type")
		with self.assertRaises(ValueError):
			text_node_to_html_node(node)
#def text_node_to_html_node(text_node):
       # if text_node.text_type == TextType.TEXT:
             #   return LeafNode(None, text_node.text)
       # elif text_node.text_type == TextType.BOLD:
            #    return LeafNode("b", text_node.text)
       # elif text_node.text_type == TextType.ITALIC:
             #   return LeafNode("i", text_node.text)
       # elif text_node.text_type == TextType.CODE:
        #        return LeafNode("code", text_node.text)
       # elif text_node.text_type == TextType.LINK:
        #        props = {"href": text_node.url}
         #       return LeafNode("a", text_node.text, props)
       # elif text_node.text_type == TextType.IMAGE:
        #        props = {
         #               "src": text_node.url,
          #              "alt": text_node.text
           #     }
            #    return LeafNode("img", "", props)
        #else:
          #      raise ValueError(f"Invalid text type: {text_node.text_type}")
