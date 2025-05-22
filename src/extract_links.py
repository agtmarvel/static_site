
from htmlnode import *
from text_types import TextNode, TextType
from textnode_to_htmlnode import *
from textnode import *
from split_delimiter import *
from block_types import *
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


#markdown to blocks

def markdown_to_blocks(markdown):
	raw_blocks = markdown.split('\n\n')

	blocks = [block.strip() for block in raw_blocks if block.strip()]

	return blocks

#helper function
def text_to_children(text):
	text_nodes = text_to_textnodes(text)
 
	html_nodes = []
	for text_node in text_nodes:
		html_node = text_node_to_html_node(text_node)
		html_nodes.append(html_node)
	return html_nodes
	
#blocks to html
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    
    parent = HTMLNode("div", None, None, [])
    
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            node = HTMLNode("p", None, None, [])
            node.children = text_to_children(block)
            parent.children.append(node)
            
        elif block_type == BlockType.HEADING:
            #determining heading level (h1-6)
            level = 0
            for char in block:
                if char == '#':
                    level += 1 
                else:
                    break
            node = HTMLNode(f"h{level}", None, None, [])
            content = block[level+1:]
            node.children = text_to_children(content)
            parent.children.append(node)
            if line != lines[-1]:
                parent.children.append(HTMLNode(None, "\n", None, []))
            
        elif block_type == BlockType.CODE:
            lines = block.split("\n")
            if len(lines) >= 2:
                code_content = "\n".join(lines[1:-1])
                text_node = TextNode(code_content, TextType.TEXT)
                code_node = text_node_to_html_node(text_node)
                pre_node - HTMLNode("pre", None, None, [code_node])
                parent.children.append(pre_node)
        
        elif block_type == BlockType.QUOTE:
            node = HTMLNode("blockquote", None, None, [])
            lines = block.split("\n")
            cleaned_lines = []
            for line in lines:
                if line.startswith(">"):
                    cleaned_line = line[1:].lstrip()
                    cleaned_lines.append(cleaned_line)
                else:
                    cleaned_lines.append(line)
                    
                content = "\n".join(cleaned_lines)
                node.children = text_to_children(content)
                parent.children.append(node)
                
        elif block_type == BlockType.ORDERED_LIST:
            ol_node = HTMLNode("ol", None, None, [])
            lines = block.split("\n")
            for line in lines:
                if not line.strip():
                    continue
                position = 0
                for i, char in enumerate(line):
                    if char == '.' and i > 0 and line [i-1].isdigit():
                        position = i + 1
                        break
                content = line[position:].strip()
                li_node = HTMLNode("li", None, None, [])
                li_node.children = text_to_children(content)
                ol_node.children.append(li_node)
            parent.children.append(ol_node)
            
        elif block_type == BlockType.UNORDERED_LIST:
            ul_node = HTMLNode("ul", None, None, [])
            lines = block.split("\n")
            for line in lines:
                if not line.strip():
                    continue
                position = 0
                if line.startswith("- "):
                    position = 2
                elif line.startswith("* "):
                    position = 2
                elif line.startswith("+ "):
                    position = 2
                content = line[position:].strip()
                li_node = HTMLNode("li", None, None, [])
                li_node.children = text_to_children(content)
                ul_node.children.append(li_node)
            parent.children.append(ul_node)
	
        
    return parent
            