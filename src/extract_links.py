
from htmlnode import *
from text_types import TextNode, TextType
from split_delimiter import *
import re
from enum import Enum

def extract_markdown_images(text):
	
	pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
	
	matches = re.findall(pattern, text)
	result = []
	for image_text, image_url in matches:
		result.append((image_text, TextType.IMAGE, image_url))
	return result

def extract_markdown_links(text):
	
	pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
	
	matches = re.findall(pattern, text)
	result = []
	for link_text, link_url in matches:
		result.append((link_text,TextType.LINK, link_url))

	return result


#split images and links

def split_nodes_image(old_nodes):
	#Create list to store new nodes
	new_nodes = []
	#Loop through each node in old_nodes(an inputted list)
	for old_node in old_nodes:
		if old_node.text_type != TextType.TEXT:
			new_nodes.append(old_node)
			continue

		images = extract_markdown_images(old_node.text)

		if not images:
			new_nodes.append(old_node)
			continue
		
		#splitting logic
		remaining_text = old_node.text
		for image_alt, text_type, image_url in images:
			image_markdown = f"![{image_alt}]({image_url})"
			parts = remaining_text.split(image_markdown, 1)
			if parts[0]:
				new_nodes.append(TextNode(parts[0], TextType.TEXT))
			new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
			if len(parts) > 1:
				remaining_text = parts[1]
			else:
				remaining_text = ""
		if remaining_text:
			new_nodes.append(TextNode(remaining_text, TextType.TEXT))

	return new_nodes


def split_nodes_link(old_nodes):
	        #Create list to store new nodes
	new_nodes = []
        #Loop through each node in old_nodes(an inputted list)
	for old_node in old_nodes:
		if old_node.text_type != TextType.TEXT:
			new_nodes.append(old_node)
			continue

		links = extract_markdown_links(old_node.text)

		if not links:
			new_nodes.append(old_node)
			continue

		remaining_text = old_node.text
		for link_text, text_type, link_url in links:
			link_markdown = f"[{link_text}]({link_url})"
			parts = remaining_text.split(link_markdown, 1)
			if parts[0]:
				new_nodes.append(TextNode(parts[0], TextType.TEXT))
			new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
			if len(parts) > 1:
				remaining_text = parts[1]
			else:
				remaining_text = ""
		if remaining_text:
			new_nodes.append(TextNode(remaining_text, TextType.TEXT))
	return new_nodes
