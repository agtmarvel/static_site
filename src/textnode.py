from enum import Enum
import re
from text_types import TextNode, TextType
from split_delimiter import *
from extract_links import *
from htmlnode import *

#text to textnode functions
def text_to_textnodes(text):
	nodes = [TextNode(text, TextType.TEXT)]
	
	nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
	nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
	nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
	nodes = split_nodes_image(nodes)
	nodes = split_nodes_link(nodes)

	return nodes
