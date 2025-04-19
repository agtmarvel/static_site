from htmlnode import *
from textnode import *
from enum import Enum

def text_node_to_html_node(text_node):
	if text_node.text_type == TextType.TEXT:
		return LeafNode(None, text_node.text)
	elif text_node.text_type == TextType.BOLD:
		return LeafNode("b", text_node.text)
	elif text_node.text_type == TextType.ITALIC:
		return LeafNode("i", text_node.text)
	elif text_node.text_type == TextType.CODE:
		return LeafNode("code", text_node.text)
	elif text_node.text_type == TextType.LINK:
		props = {"href": text_node.url}
		return LeafNode("a", text_node.text, props)
	elif text_node.text_type == TextType.IMAGE:
		props = {
			"src": text_node.url,
			"alt": text_node.text
		}
		return LeafNode("img", "", props)
	else:
		raise ValueError(f"Invalid text type: {text_node.text_type}")



#class LeafNode(HTMLNode):
    #def __init__(self, tag, value, props=None):
        # Call the parent constructor with children=None
        #super().__init__(tag, value, None, props)
