
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
	
#from htmlnode import *
#from textnode import *
#from enum import Enum

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
