from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	result = []
	for old_node in old_nodes:
		if old_node.text_type != TextType.TEXT:
			result.append(old_node)
			continue
		
		current_text = old_node.text

		while delimiter in current_text:
			start_index = current_text.find(delimiter)
		
			end_index = current_text.find(delimiter, start_index + len(delimiter))
		
			if end_index == -1:
				raise ValueError(f"No closing delimiter '{delimiter}' found")
		
			before = current_text[:start_index]
			inside = current_text[start_index + len(delimiter):end_index]
			after = current_text[end_index + len(delimiter):]

			if before:
				result.append(TextNode(before, TextType.TEXT))
			
			result.append(TextNode(inside, text_type))

			current_text = after
		
		if current_text:
			result.append(TextNode(current_text, TextType.TEXT))

			
	return result
